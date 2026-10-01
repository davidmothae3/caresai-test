**INTRODUCTION OF THE PROJECT**

**CARES: Climate Anticipatory Risk and Early Warning System**

TitaniumX Group | Mohloli Innovation Hub

Children across Lesotho face a growing convergence of climate sensitive health threats, including diarrhoeal disease, acute respiratory infections, hypothermia, and severe acute malnutrition. These risks are shaped not only by poverty and access to services, but also by climate variability and environmental vulnerability. Rainfall anomalies, drought conditions, temperature drops, flooding, and snow related road disruption can all affect whether vulnerable children receive timely care and essential services. Yet very few climate and health platforms have been designed from within Lesotho to anticipate these risks before they escalate.

CARES is an open source, AI powered anticipatory intelligence platform (CARE-AI) designed to answer one operational question: given current and forecast climate conditions, what child health risks are likely to emerge in the next two to four weeks, where will they occur, and what action should be taken before impacts escalate?

Built on a modular architecture designed for DHIS2 integration, CARES combines climate data, child health indicators, geospatial analysis, machine learning, and explainable AI to generate district risk classifications, preparedness alerts, and decision support outputs. Its predictive engine, CARE AI, uses classification models to identify elevated risk districts before disease burden increases. Risk intelligence is presented through an interactive dashboard and a planned community alert layer, RiSe, intended for future use by community health workers and local response systems.

CARES has progressed beyond concept stage into a functioning prototype developed in Lesotho by TitaniumX Group. The prototype uses notional and DHS anchored data to demonstrate predictive feasibility, model explainability, district risk mapping, and dashboard based alert generation. It does not use individual child records and should not be interpreted as a validated clinical or epidemiological prediction system. 

As the flagship platform of the Mohloli innovation ecosystem, CARES represents an Africa built digital public infrastructure concept grounded in local disease burden, local data realities, and local ownership. It is designed to support future government integration, open source collaboration, phased national scale up, and adaptation to other climate vulnerable settings.


**Technologies used in the prototype**

Here's a summary of the technologies used in this project and their functions:

**pandas (pd)**: Utilized for efficient data manipulation and analysis, such as loading CSV files, handling missing values (dropna), encoding categorical features, and managing DataFrames.

**NumPy (np):** Used for numerical operations, especially in array manipulation (e.g., np.argmax for CNN predictions) and statistical calculations.

**Matplotlib (plt) & Seaborn (sns):** Essential for data visualization, creating plots such as distribution plots (countplot), confusion matrices, feature importance bar charts, and scatter plots.

**Scikit-learn (sklearn):** A comprehensive machine learning library used for:

**train_test_split:** Dividing data into training and testing sets.

**StandardScaler:** Feature scaling to standardize data.

**RandomForestClassifier:** Implementing the Random Forest model for classification.

**classification_report, confusion_matrix, accuracy_score, roc_auc_score:** Evaluating model performance with various metrics.

**KFold:** Performing cross-validation for model stability assessment.

**Imbalanced-learn (imblearn.over_sampling.SMOTE):** Addressing class imbalance in the dataset by oversampling the minority classes.

**TensorFlow/Keras (tensorflow.keras):** The deep learning framework used for:

**Sequential:** Building the Convolutional Neural Network (CNN) model layer by layer.

**Conv1D, MaxPooling1D, Flatten, Dense, Dropout:** Defining the architecture of the CNN, including convolutional layers, pooling, flattening, dense layers, and dropout for regularization.
Model compilation (compile) and training (fit).

**XGBoost (xgboost, XGBClassifier):** An optimized gradient boosting library used for building the XGBoost Classifier model, known for its performance and efficiency.

**ELI5 (eli5, eli5.sklearn.PermutationImportance):** A library for debugging machine learning classifiers and explaining their predictions, specifically used here for Permutation Importance to understand feature relevance in the CNN.

**SHAP (shap, shap.GradientExplainer):** A powerful tool for explaining the output of any machine learning model. It was used with GradientExplainer to provide local and global explanations of the CNN's predictions through SHAP values and summary plots.

**json:** For working with JSON data, specifically for structuring and printing the project_summary dictionary.


**The CARES DEMO RESULTS**

**Model Performance and Comparison**


All three models demonstrated strong performance in classifying 'risk_level', with the XGBoost Classifier emerging as the top performer.

Convolutional Neural Network (CNN):

Test Accuracy: 0.9214 Weighted ROCAUC: 0.9750 Mean Cross-Validation Accuracy: 0.9508 (+/- 0.0075), indicating good stability. 

Random Forest Classifier:

Test Accuracy: 0.95 Weighted ROCAUC: 0.9877

XGBoost Classifier (Best Performing Model):

Test Accuracy: 0.9705 Weighted ROCAUC: 0.9954 XGBoost significantly outperformed both the CNN and Random Forest in terms of both accuracy and ROCAUC, demonstrating its superior predictive power for this task.

**Feature Importance Analysis**

The feature importance analyses across all models (Permutation Importance & SHAP for CNN, intrinsic importance for Random Forest and XGBoost) converged on several key factors:

Consistently Important Features:

Features such as diarrhoea_rate_per1000, rainfall_mm, ari_rate_per1000, urban_pct, and mean_altitude_m were repeatedly identified as highly influential by all models, especially by XGBoost. Key Drivers of Risk: Generally, indicators related to public health (like diarrhoea_rate_per1000, ari_rate_per1000, sam_rate_per1000) and environmental factors (like rainfall_mm, temperature_mean_c) played critical roles in predicting risk levels. Infrastructure-related features (safe_water_pct, improved_sanit_pct) also showed high importance.
Data schema
CARES.csv (4,068 rows × 29 columns)
One row per community per month: 113 communities (96 distinct names; some placeholder names repeat across districts) × 36 months (2022–2024), across 10 districts.

Group	Columns
Identifiers	year, month, district, community, record_type
Context	elevation_zone, highland, mean_altitude_m, urban_pct, u5_population
Climate	rainfall_mm, temperature_min_c, temperature_max_c, temperature_mean_c, frost_days, spi_drought_index, snow_access_risk
Child health	diarrhoea_rate_per1000, diarrhoea_cases_u5, ari_rate_per1000, ari_cases_u5, sam_rate_per1000, sam_cases_u5
Water, sanitation, nutrition	safe_water_pct, improved_sanit_pct, stunting_pct_dhs, wasting_pct_dhs
Labels	risk_score, risk_level (Low < 45, Medium 45–69.9, High ≥ 70)
Model inputs (17): rainfall_mm, temperature_mean_c, frost_days, spi_drought_index, snow_access_risk, the six child-health columns, safe_water_pct, improved_sanit_pct, stunting_pct_dhs, wasting_pct_dhs, mean_altitude_m, urban_pct. The target is risk_level. risk_score is excluded from the inputs to prevent label leakage.

care_ai_output.json
Level	Fields
Top level	generated_at, model_version, model_architecture, rf_accuracy, cnn_accuracy, cnn_high_risk_recall, cross_validation_mean, data_source, districts, trends
districts[name]	district, risk_score, risk_level, confidence, diarrhoea_rate, ari_rate, rainfall, safe_water, temp, highland, u5_population, lat, lng, communities
communities[]	name, risk_score, risk_level, diarrhoea_rate, ari_rate, rainfall, safe_water, temp, highland, u5_pop
trends[name]	Monthly risk-score series (12 values)


**Conclusion**

The analysis confirms that advanced machine learning techniques are highly effective for risk level prediction in this context. The XGBoost Classifier stands out as the most robust and accurate model among those evaluated. The consistent identification of key features across different model architectures provides strong insights into the underlying drivers of risk, which can inform targeted interventions and decision-making.


