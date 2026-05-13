**INTRODUCTION OF THE PROJECT**
(TTXGROUP contribution)




**RESULTS** 

I have implement a Convolutional Neural Network (CNN) on our dataset. Since our data is tabular, I adapted it by reshaping the features to be suitable for a 1D CNN. We'll use the risk_level as the target variable for this classification task. After defining and training the model, I'll evaluate its performance with a classification report and a confusion matrix.

The CNN model for predicting risk_level has been trained and evaluated.

Here are the performance metrics:

<img width="735" height="393" alt="image" src="https://github.com/user-attachments/assets/d39379d1-de63-45c3-a7f3-d18408e097c4" />




The model demonstrates strong performance, especially for risk_level 1, with a high overall accuracy. The confusion matrix also provides a visual representation of the model's predictions versus the actual values.

We've made significant progress in analyzing your dataset and building predictive models. Here's a summary of what we've accomplished:

Data Preprocessing and Cleaning: We started by importing your CARES.csv dataset, handling missing values, and encoding categorical features like elevation_zone, highland, and risk_level into numerical representations. We also dropped non-numerical and non-contributing columns (year, month, district, community, record_type, u5_population, temperature_min_c, temperature_max_c).

Convolutional Neural Network (CNN) for Tabular Data (Target: risk_level): Most recently, we implemented and evaluated a 1D CNN model.

Performance: The CNN achieved a Test Loss of 0.1375 and a Test Accuracy of 0.9484. The classification report showed strong performance, with high precision, recall, and f1-scores for the different risk_level classes (e.g., 0.97 f1-score for class 1).
Confusion Matrix: The confusion matrix indicated that the CNN model made only a few misclassifications, demonstrating good predictive capabilities.

**Explainable AI**


To provide a more comprehensive understanding of your CNN model's predictions, I will apply SHAP (SHapley Additive exPlanations). SHAP is a powerful method that explains the contribution of each feature to a prediction. This will help us understand which features are most important for the CNN's output, both globally and for individual predictions.


**VALIDATION**
To ensure the stability and robustness of our CNN model, I will now implement k-fold cross-validation. This will give us a more reliable estimate of its performance across different subsets of the training data.

The cross-validation for the CNN model has completed successfully! Here are the results:

Mean Validation Accuracy: This model achieved an average validation accuracy of 0.9690 (or 96.90%) across the 5 folds.
Standard Deviation of Accuracy: The accuracy varied by +/- 0.0074, which suggests that the model is quite stable and its performance is consistent across different subsets of the data.
Mean Validation Loss: The average validation loss was 0.0813.
Standard Deviation of Loss: The loss varied by +/- 0.0111, also indicating good stability.
These results demonstrate that the CNN model is robust and generalizes well to unseen data, as indicated by the high mean accuracy and low standard deviations for both accuracy and loss
