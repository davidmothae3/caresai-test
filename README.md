# CARES — Climate Anticipatory Risk and Early Warning System

**Open-source anticipatory intelligence for child health risk in Lesotho.**

Built by TitaniumX Group (Pty) Ltd through the Mohloli Digital and Innovation Hub (MDI Hub), Maseru, Lesotho.

Live dashboard: https://davidmothae3.github.io/caresai-test/ · Code licence: MIT

---

## 1. What CARES is

CARES combines climate, child-health and geographic indicators to classify district and community risk (Low / Medium / High) across Lesotho's 10 districts and 113 communities, explains each classification, and suggests a preparedness action. The intended use is anticipatory action: district health teams see where risk is rising, why, and what to do before disease burden escalates. Its prediction engine is called CARE-AI.

**Status.** CARES is a functioning prototype. It runs on a notional, DHS-anchored dataset. It contains no individual child records, is not connected to DHIS2 or any live health system, and is not a validated clinical or epidemiological tool. Results demonstrate technical feasibility only (see [Limitations](#9-limitations)).

## 2. Repository contents

| File | Purpose |
|---|---|
| `CARES.csv` | Notional, DHS-anchored dataset: 4,068 rows × 29 columns (see [schema](#4-data-schema)) |
| `Climate_Health_Risk_Kids_Under_5.ipynb` | Google Colab notebook: preprocessing, SMOTE, Random Forest, 1D-CNN, SHAP, cross-validation |
| `care_ai_output.json` | Model output consumed by the dashboard (district scores, community records, confidence, monthly trends) |
| `index.html` | Single-file dashboard (Leaflet, Chart.js). Also embeds GIS reference layers |
| `LICENSE` | MIT licence, © 2026 TitaniumX Group (Pty) Ltd |
| `.github/redeploy-trigger.txt` | Used to trigger a GitHub Pages redeploy; no runtime function |

## 3. Pipeline

```
CARES.csv → notebook (preprocess → SMOTE → Random Forest + 1D-CNN → SHAP) → care_ai_output.json → index.html (dashboard)
```

1. **Data.** `CARES.csv` holds one row per community per month, 2022–2024.
2. **Modelling.** The notebook encodes and cleans the data, splits it 80/20, balances the training set with SMOTE, and trains a Random Forest and a 1D-CNN to classify `risk_level`. SHAP explains the CNN's predictions.
3. **Export.** `care_ai_output.json` contains model metadata, district scores, community records, confidence values and monthly trends. The file in this repository is a committed export of the model output (generated 2026-05-16). A final notebook cell that regenerates it from the trained model is being added; until it is committed, the JSON is not produced by a notebook cell.
4. **Dashboard.** `index.html` fetches `care_ai_output.json` on load. If the file cannot be loaded, it falls back to an embedded notional dataset.

## 4. Data schema

### `CARES.csv` (4,068 rows × 29 columns)

One row per community per month: 113 communities (96 distinct names; some placeholder names repeat across districts) × 36 months (2022–2024), across 10 districts.

| Group | Columns |
|---|---|
| Identifiers | `year`, `month`, `district`, `community`, `record_type` |
| Context | `elevation_zone`, `highland`, `mean_altitude_m`, `urban_pct`, `u5_population` |
| Climate | `rainfall_mm`, `temperature_min_c`, `temperature_max_c`, `temperature_mean_c`, `frost_days`, `spi_drought_index`, `snow_access_risk` |
| Child health | `diarrhoea_rate_per1000`, `diarrhoea_cases_u5`, `ari_rate_per1000`, `ari_cases_u5`, `sam_rate_per1000`, `sam_cases_u5` |
| Water, sanitation, nutrition | `safe_water_pct`, `improved_sanit_pct`, `stunting_pct_dhs`, `wasting_pct_dhs` |
| Labels | `risk_score`, `risk_level` (Low < 45, Medium 45–69.9, High ≥ 70) |

**Model inputs (17):** `rainfall_mm`, `temperature_mean_c`, `frost_days`, `spi_drought_index`, `snow_access_risk`, the six child-health columns, `safe_water_pct`, `improved_sanit_pct`, `stunting_pct_dhs`, `wasting_pct_dhs`, `mean_altitude_m`, `urban_pct`. The target is `risk_level`. `risk_score` is excluded from the inputs to prevent label leakage.

### `care_ai_output.json`

| Level | Fields |
|---|---|
| Top level | `generated_at`, `model_version`, `model_architecture`, `rf_accuracy`, `cnn_accuracy`, `cnn_high_risk_recall`, `cross_validation_mean`, `data_source`, `districts`, `trends` |
| `districts[name]` | `district`, `risk_score`, `risk_level`, `confidence`, `diarrhoea_rate`, `ari_rate`, `rainfall`, `safe_water`, `temp`, `highland`, `u5_population`, `lat`, `lng`, `communities` |
| `communities[]` | `name`, `risk_score`, `risk_level`, `diarrhoea_rate`, `ari_rate`, `rainfall`, `safe_water`, `temp`, `highland`, `u5_pop` |
| `trends[name]` | Monthly risk-score series (12 values) |

## 5. Models and results

Random 80/20 split (`random_state=42`): 3,254 training rows and 814 test rows (test support: Low 140, Medium 596, High 78). SMOTE is applied to the training set only (3,254 → 6,897 rows). The CNN is a 1D convolutional network over the 17 inputs reshaped to (17, 1).

| Metric | Random Forest | CNN |
|---|---|---|
| Test accuracy | 95% | 92% |
| High-Risk recall | 86% | 96% |
| High-Risk precision | 88% | 74% |
| Weighted F1 | 0.95 | 0.92 |
| 5-fold cross-validation, mean accuracy | — | 94.6% |

Per-class precision / recall on the test set:

| Class | Random Forest | CNN |
|---|---|---|
| Low | 0.89 / 0.94 | 0.87 / 0.87 |
| Medium | 0.97 / 0.96 | 0.96 / 0.92 |
| High | 0.88 / 0.86 | 0.74 / 0.96 |

**Note on figures.** The 94.6% cross-validation figure is the CNN result printed by the committed notebook and stored in `care_ai_output.json`. Earlier documents, including our proposal, quote 96.9% ± 0.74% from an earlier run of the same 5-fold procedure. This README reports the committed notebook output.

**Explainability.** SHAP explains the CNN's predictions (global and per-prediction). Feature-importance analysis is applied to the Random Forest. The dashboard shows the top drivers behind each district's score.

## 6. Dashboard

`index.html` provides three views:

- **District Risk Map:** risk by district and community, drill-down panels with metrics, top drivers and recommended action, and a district rainfall forecast panel.
- **Trend Analysis:** 2024 monthly risk-score trends by district, with High (≥ 70) and Medium (≥ 45) reference lines.
- **Alert Feed:** districts ranked by risk score with top drivers and forecast rainfall. Alert times shown in the feed ("4m ago" and similar) are illustrative in the prototype; there is no live alerting yet.

Map layers:

- 113 community markers, coloured by risk. Some markers use approximate positions and are drawn with dashed outlines.
- 202 health facilities and 2,393 schools (official Lesotho datasets), toggled independently and clustered.
- 78 Community Council boundaries (FAO/MLGCA 2019) as a GIS reference layer, with click-to-filter drill-down. Council polygons are **not** linked to model risk scores.

The forecast panel calls the OpenWeatherMap 5-day forecast for each district centroid and shows daily rainfall. It is independent of the risk model: the model does not use live weather.

## 7. Running locally

**Dashboard.** Serve the folder over HTTP (opening `index.html` directly from disk blocks the JSON request):

```bash
python -m http.server 8000
# open http://localhost:8000
```

**Notebook.** Open `Climate_Health_Risk_Kids_Under_5.ipynb` in Google Colab, upload `CARES.csv`, and run all cells. Dependencies:

```bash
pip install pandas numpy scikit-learn imbalanced-learn tensorflow shap eli5 xgboost matplotlib seaborn
```

## 8. Data, licence and governance

- **Code:** MIT licence (see `LICENSE`).
- **Data in this repository:** `CARES.csv` is a notional dataset anchored to aggregate Lesotho DHS 2023–24 indicators. It contains aggregated community-month rows and no individual records.
- **Protected data:** No Ministry of Health or DHIS2 data is stored in this repository. Real operational data will remain protected under a data-sharing agreement and will not be committed.
- **GIS layers:** Facility, school and Community Council layers embedded in `index.html` derive from official Lesotho datasets and FAO/MLGCA (2019) boundaries and remain subject to their providers' terms. The MIT licence covers the code.
- **Weather API:** The dashboard currently calls OpenWeatherMap directly from the browser with a free-tier key. This is a prototype trade-off; the call will move behind a server-side proxy.

## 9. Limitations

- **Notional data and synthetic labels.** `risk_score` and `risk_level` are labels defined in the notional dataset (a threshold on `risk_score`), not observed health outcomes.
- **Classifies current risk.** Model inputs are same-month indicators and include disease rates, so the prototype classifies current risk. It is not yet a forecasting model. Lagged climate features for forecasting are planned.
- **Optimistic validation.** Results come from a random train/test split and k-fold cross-validation on one notional dataset. Temporal hold-out and leave-one-district-out validation have not yet been run.
- **Placeholder geography.** Some community names repeat across districts and some marker positions are approximate. Real boundaries will come with real data.
- **Access risk not yet modelled.** Health-facility and school locations are mapped, and Community Council boundaries are shown for reference. A predictive road and school access-disruption model is not yet built.
- **Live weather is display-only.** The forecast panel is not an input to the risk model.
- **Alerts are illustrative.** The Alert Feed ranks districts from the exported scores and shows illustrative timestamps. SMS and other alert delivery are on the roadmap (Q4).
- **Not a clinical tool.** Outputs support planning decisions and are not diagnostic.

## 10. Roadmap

| Quarter | Focus |
|---|---|
| Q1 | DHIS2 data-sharing agreement and connector; validation across all 10 districts; open-source documentation and replication toolkit; production hosting |
| Q2 | ARI and hypothermia module, deployed to highland districts ahead of winter |
| Q3 | Nutrition and food-security module (drought indicators, LVAC data); scoping of a multi-hazard module with the Disaster Management Authority |
| Q4 | SMS alerts to community health workers; road and school access-disruption model; full Ministry of Health integration; replication toolkit for other countries |

## 11. Team and contributors

| Name | Role |
|---|---|
| Akinyemi Atobatele | Program Lead / CEO |
| Palo Moshoeshoe | Technical Architect / Lead AI |
| Joel Nimarko | GIS Specialist |
| David Mothae | Mohloli Digital and Innovation Hub Lead (dashboard and delivery) |
| Thulo Monyatsi | DHIS2 integration and backend |

Commit history appears under three GitHub accounts: `nongolosh` (Palo Moshoeshoe), and `davidmothae3` and `RudraDav3` (David Mothae).

TitaniumX Group (Pty) Ltd · Maseru, Lesotho
