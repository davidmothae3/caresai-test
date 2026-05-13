
** RESULTS** 
I have implement a Convolutional Neural Network (CNN) on our dataset. Since our data is tabular, I adapted it by reshaping the features to be suitable for a 1D CNN. We'll use the risk_level as the target variable for this classification task. After defining and training the model, I'll evaluate its performance with a classification report and a confusion matrix.

The CNN model for predicting risk_level has been trained and evaluated.

Here are the performance metrics:

CNN Test Loss: 0.1375
CNN Test Accuracy: 0.9484
Classification Report:

              precision    recall  f1-score   support

           0       0.99      0.82      0.90       140
           1       0.95      0.98      0.97       596
           2       0.89      0.91      0.90        78

    accuracy                           0.95       814
   macro avg       0.94      0.90      0.92       814
weighted avg       0.95      0.95      0.95       814
The model demonstrates strong performance, especially for risk_level 1, with a high overall accuracy. The confusion matrix also provides a visual representation of the model's predictions versus the actual values.

We've made significant progress in analyzing your dataset and building predictive models. Here's a summary of what we've accomplished:

Data Preprocessing and Cleaning: We started by importing your CARES.csv dataset, handling missing values, and encoding categorical features like elevation_zone, highland, and risk_level into numerical representations. We also dropped non-numerical and non-contributing columns (year, month, district, community, record_type, u5_population, temperature_min_c, temperature_max_c).

Random Forest Classifier (Target: risk_level): We trained a Random Forest Classifier to predict risk_level.

Initial Results: The model initially showed perfect scores (1.00 accuracy, precision, recall, f1-score). I raised a concern about potential data leakage or overfitting due to these unusually high scores.
Feature Importance: risk_score was identified as the most important feature (0.50), followed by diarrhoea_rate_per1000 (0.16) and rainfall_mm (0.10).
Confusion Matrix: The confusion matrix for this model confirmed perfect classification across all risk levels, reinforcing the concern about data leakage.
Random Forest Regressor (Target: risk_score): We then shifted focus to a regression task, predicting risk_score using a RandomForestRegressor.

Performance: This model performed very well, achieving an R-squared of 0.9898, a Mean Absolute Error (MAE) of 0.7646, and a Mean Squared Error (MSE) of 1.1298.
Feature Importance: For the regression task, diarrhoea_rate_per1000 emerged as the most important feature (0.75), followed by rainfall_mm (0.10) and ari_rate_per1000 (0.10).
Convolutional Neural Network (CNN) for Tabular Data (Target: risk_level): Most recently, we implemented and evaluated a 1D CNN model.

Performance: The CNN achieved a Test Loss of 0.1375 and a Test Accuracy of 0.9484. The classification report showed strong performance, with high precision, recall, and f1-scores for the different risk_level classes (e.g., 0.97 f1-score for class 1).
Confusion Matrix: The confusion matrix indicated that the CNN model made only a few misclassifications, demonstrating good predictive capabilities.
