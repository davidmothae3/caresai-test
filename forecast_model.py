# CARES 1-month-ahead forecast: run in the folder that contains CARES.csv
# pip install pandas numpy scikit-learn xgboost

# ---- 1) leak-free lagged features ----
import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings('ignore')
from sklearn.metrics import accuracy_score, f1_score, mean_absolute_error, recall_score, precision_score, confusion_matrix, roc_auc_score
from xgboost import XGBRegressor, XGBClassifier
from sklearn.ensemble import RandomForestRegressor
lvl=lambda s: np.where(s>=70,2,np.where(s>=45,1,0))
df=pd.read_csv('CARES.csv')
df['highland']=df['highland'].astype(str).str.upper().map({'FALSE':0,'TRUE':1})
df['elev']=df['elevation_zone'].map({'lowland':0,'foothill':1,'highland':2})
df['t']=(df.year-2022)*12+df.month
df['cid']=df.district+'|'+df.community
df=df.sort_values(['cid','t']).reset_index(drop=True)
assert df.groupby('cid').size().eq(36).all(), df.groupby('cid').size().value_counts()
dyn=['rainfall_mm','temperature_mean_c','frost_days','spi_drought_index','snow_access_risk','diarrhoea_rate_per1000','ari_rate_per1000','sam_rate_per1000','risk_score']
stat=['elev','highland','mean_altitude_m','urban_pct','safe_water_pct','improved_sanit_pct','stunting_pct_dhs','wasting_pct_dhs','u5_population']
g=df.groupby('cid')
F=df[['cid','district','community','t','month','risk_score']+stat].copy()
for c in dyn:
    F[c]=df[c]; F[c+'_l1']=g[c].shift(1); F[c+'_l2']=g[c].shift(2)
F['score_ly']=g['risk_score'].shift(11)   # value at same calendar month as the forecast target (t+1), one year earlier = t-11
F['score_delta']=F['risk_score']-F['risk_score_l1']
F['m_sin']=np.sin(2*np.pi*(F.month%12+1)/12); F['m_cos']=np.cos(2*np.pi*(F.month%12+1)/12)   # month of the TARGET
F['next_score']=g['risk_score'].shift(-1)
F['next_rain']=g['rainfall_mm'].shift(-1); F['next_temp']=g['temperature_mean_c'].shift(-1)
F.to_pickle('F.pkl')
print(F.shape, F.next_score.notna().sum())


# ---- 2) time-split evaluation setup ----
import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings('ignore')
from sklearn.metrics import accuracy_score, f1_score, mean_absolute_error, recall_score, precision_score, confusion_matrix, roc_auc_score
from xgboost import XGBRegressor, XGBClassifier
lvl=lambda s: np.where(np.asarray(s)>=70,2,np.where(np.asarray(s)>=45,1,0))
F=pd.read_pickle('F.pkl')
D=F.dropna(subset=['next_score']).copy()
tr=D[D.t<=23]; te=D[D.t>=24]
print('train',len(tr),'test',len(te),'test targets months',sorted((te.t+1).unique()))
ytr,yte=tr.next_score,te.next_score; ltest=lvl(yte)
base=[c for c in F.columns if c not in('cid','district','community','next_score','next_rain','next_temp','t','month')]
featA=base; featB=base+['next_rain','next_temp']
def rep(name,pred):
    pl=lvl(pred); 
    print(f"{name:34} MAE {mean_absolute_error(yte,pred):5.2f}  acc {accuracy_score(ltest,pl):.3f}  macroF1 {f1_score(ltest,pl,average='macro'):.3f}  Hrecall {recall_score(ltest==2,pl==2):.2f} Hprec {precision_score(ltest==2,pl==2,zero_division=0):.2f}  Lrecall {recall_score(ltest==0,pl==0):.2f}")
    return pl


# ---- 3) backtest tables + Jan 2025 forecast (writes forecast.json) ----

from sklearn.metrics import roc_auc_score
def mk(ft,trn,seed=42): return XGBRegressor(n_estimators=400,max_depth=4,learning_rate=0.05,subsample=0.8,colsample_bytree=0.8,random_state=seed).fit(trn[ft],trn.next_score)
TH=60  # High-alert threshold chosen on 2023 inner validation (see ev2.py)
mA=mk(featA,tr); pA=mA.predict(te[featA]); mB=mk(featB,tr); pB=mB.predict(te[featB])
clim=te.m_sin.map(tr.groupby('m_sin').next_score.mean()).values
sn=te.score_ly.values; sn=np.where(np.isnan(sn),clim,sn)
def row(name,p,th=None):
    pl=lvl(p); hp=(p>=th) if th else (pl==2)
    return dict(name=name,mae=round(float(mean_absolute_error(yte,p)),2),acc=round(float(accuracy_score(ltest,pl)),3),f1=round(float(f1_score(ltest,pl,average='macro')),3),
      auc=round(float(roc_auc_score(ltest==2,p)),3),hrec=round(float(recall_score(ltest==2,hp)),2),hprec=round(float(precision_score(ltest==2,hp,zero_division=0)),2))
tab=[row('Persistence (next month = this month)',te.risk_score.values,TH),row('Climatology (average for that month)',clim,TH),row('Seasonal naive (same month last year)',sn,TH),
     row('XGBoost forecast',pA,TH),row('XGBoost + climate outlook*',pB,TH)]
# High recall/precision for baselines use their own level==High rule (th None) ; forecast rows use TH alert
cmA=confusion_matrix(ltest,lvl(pA)).tolist()
e=(yte.values-pA)
te2=te.assign(p=pA,tm=te.t+1)
monthly=[[int(tm-24),round(float(mean_absolute_error(g.next_score,g.p)),2),round(float(mean_absolute_error(g.next_score,g.risk_score)),2)] for tm,g in te2.groupby('tm')]
# district-level backtest
def wavg(g,c): return np.average(g[c],weights=g.u5_population)
dm=te2.groupby(['district','tm']).apply(lambda g: pd.Series(dict(p=wavg(g,'p'),a=wavg(g,'next_score'),n=wavg(g,'risk_score')))).reset_index()
ed=(dm.a-dm.p).values
dist_bt=dict(mae=round(float(np.abs(ed).mean()),2),mae_persist=round(float(np.abs(dm.a-dm.n).mean()),2))
imp=sorted(zip(featA,mA.feature_importances_),key=lambda x:-x[1])[:10]
# final model: all data with known target, forecast Jan 2025 from Dec 2024 (t=36)
full=D; mF=mk(featA,full); cur=F[F.t==36].copy(); cur['p']=mF.predict(cur[featA])
q10,q90=np.quantile(e,[.1,.9]); qd10,qd90=np.quantile(ed,[.1,.9])
comm={}
for _,r in cur.iterrows():
    comm[r.cid]=dict(s=round(float(r.p),1),lo=round(float(r.p+q10),1),hi=round(float(r.p+q90),1),ph=round(float(np.mean(r.p+e>=70)),2),obs=round(float(r.risk_score),1))
dist={}
for d,g in cur.groupby('district'):
    p=wavg(g,'p'); o=wavg(g,'risk_score')
    dist[d]=dict(s=round(float(p),1),lo=round(float(p+qd10),1),hi=round(float(p+qd90),1),ph=round(float(np.mean(p+ed>=70)),2),obs=round(float(o),1))
out=dict(target='Jan 2025',base='Dec 2024',horizon='1 month',train='Jan 2022 – Dec 2023',test='Jan – Dec 2024',thresholdHigh=TH,n_test=int(len(te)),
 table=tab,cm=cmA,monthly=monthly,dist_bt=dist_bt,imp=[[k,round(float(v),4)] for k,v in imp],communities=comm,districts=dist,
 interval='80% range from 2024 out-of-sample errors')
json.dump(out,open('forecast.json','w'),separators=(',',':'))
for t in tab: print(t)
print('cm',cmA,'dist_bt',dist_bt); print('imp',imp[:5])
print({d:(v['obs'],v['s'],v['lo'],v['hi'],v['ph']) for d,v in dist.items()})
print('communities forecast>=70:',sum(v['s']>=70 for v in comm.values()),'of',len(comm),' size',len(json.dumps(out)))
