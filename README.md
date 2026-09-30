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





