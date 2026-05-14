**INTRODUCTION OF THE PROJECT**
(TTXGROUP contribution)




**RESULTS Convolution Neural Networks** 

I have implement a Convolutional Neural Network (CNN) on our dataset. Since our data is tabular, I adapted it by reshaping the features to be suitable for a 1D CNN. We'll use the risk_level as the target variable for this classification task. After defining and training the model, I'll evaluate its performance with a classification report and a confusion matrix.

The CNN model for predicting risk_level has been trained and evaluated.

Here are the performance metrics:

<img width="735" height="393" alt="image" src="https://github.com/user-attachments/assets/d39379d1-de63-45c3-a7f3-d18408e097c4" />

<img width="610" height="547" alt="image" src="https://github.com/user-attachments/assets/11779cef-bf0a-4076-ad30-a48498c73705" />



The model demonstrates strong performance, especially for risk_level 1, with a high overall accuracy. The confusion matrix also provides a visual representation of the model's predictions versus the actual values.

We've made significant progress in analyzing your dataset and building predictive models. Here's a summary of what we've accomplished:

Data Preprocessing and Cleaning: We started by importing your CARES.csv dataset, handling missing values, and encoding categorical features like elevation_zone, highland, and risk_level into numerical representations. We also dropped non-numerical and non-contributing columns (year, month, district, community, record_type, u5_population, temperature_min_c, temperature_max_c).

Convolutional Neural Network (CNN) for Tabular Data (Target: risk_level): Most recently, we implemented and evaluated a 1D CNN model.

Performance: The CNN achieved a Test Loss of 0.1375 and a Test Accuracy of 0.9484. The classification report showed strong performance, with high precision, recall, and f1-scores for the different risk_level classes (e.g., 0.97 f1-score for class 1).
Confusion Matrix: The confusion matrix indicated that the CNN model made only a few misclassifications, demonstrating good predictive capabilities.

**Explainable AI**
<img width="1146" height="701" alt="image" src="https://github.com/user-attachments/assets/f124819c-b945-4f2f-9139-f73a25fb134f" />


To provide a more comprehensive understanding of your CNN model's predictions, I will apply SHAP (SHapley Additive exPlanations). SHAP is a powerful method that explains the contribution of each feature to a prediction. This will help us understand which features are most important for the CNN's output, both globally and for individual predictions.
<img width="779" height="859" alt="SHAP" src="https://github.com/user-attachments/assets/b5320e0b-760b-449b-aef6-60442f020958" />


**VALIDATION**
To ensure the stability and robustness of our CNN model, I will now implement k-fold cross-validation. This will give us a more reliable estimate of its performance across different subsets of the training data.

The cross-validation for the CNN model has completed successfully! Here are the results:

Mean Validation Accuracy: This model achieved an average validation accuracy of 0.9690 (or 96.90%) across the 5 folds.
Standard Deviation of Accuracy: The accuracy varied by +/- 0.0074, which suggests that the model is quite stable and its performance is consistent across different subsets of the data.
Mean Validation Loss: The average validation loss was 0.0813.
Standard Deviation of Loss: The loss varied by +/- 0.0111, also indicating good stability.
These results demonstrate that the CNN model is robust and generalizes well to unseen data, as indicated by the high mean accuracy and low standard deviations for both accuracy and loss

**RESULTS Random Forest**

This report provides a detailed breakdown of the model's performance for each risk_level class (0, 1, 2, corresponding to Low, Medium, High Risk) and overall averages. Here's what each metric means:

Precision: For each class, precision measures the proportion of correctly predicted positive observations to the total predicted positive observations. A high precision means a low false positive rate.

Class 0 (Low Risk): 0.89 - When the model predicts 'Low Risk', it is correct 89% of the time.
Class 1 (Medium Risk): 0.97 - When the model predicts 'Medium Risk', it is correct 97% of the time.
Class 2 (High Risk): 0.88 - When the model predicts 'High Risk', it is correct 88% of the time.
Recall: For each class, recall measures the proportion of correctly predicted positive observations to all observations in the actual class. A high recall means a low false negative rate.

Class 0 (Low Risk): 0.94 - The model correctly identifies 94% of all actual 'Low Risk' instances.
Class 1 (Medium Risk): 0.96 - The model correctly identifies 96% of all actual 'Medium Risk' instances.
Class 2 (High Risk): 0.86 - The model correctly identifies 86% of all actual 'High Risk' instances.
F1-Score: The F1-Score is the harmonic mean of precision and recall. It's a useful metric when you need to balance both precision and recall, especially in cases of uneven class distribution.

Class 0 (Low Risk): 0.92
Class 1 (Medium Risk): 0.96
Class 2 (High Risk): 0.87
Support: This is the number of actual occurrences of the class in the specified dataset (in this case, the test set).

Class 0 (Low Risk): 140
Class 1 (Medium Risk): 596
Class 2 (High Risk): 78
Accuracy: The proportion of total correct predictions across all classes. The overall accuracy of the Random Forest model is 0.95, meaning it correctly predicted the risk level for 95% of the test instances.

Macro Avg: The average of precision, recall, and F1-score for all classes, treating all classes equally. It's useful when you want to see how the model performs on each class without being influenced by class imbalance.

Macro Avg Precision: 0.91
Macro Avg Recall: 0.92
Macro Avg F1-Score: 0.92
Weighted Avg: The average of precision, recall, and F1-score for all classes, weighted by the number of instances in each class. This is more representative of the overall performance when there is class imbalance.

Weighted Avg Precision: 0.95
Weighted Avg Recall: 0.95
Weighted Avg F1-Score: 0.95
In summary, the Random Forest model shows strong performance, particularly for the 'Medium Risk' class, with high precision and recall. Performance for 'Low Risk' and 'High Risk' is also very good, indicating the model generalizes well to unseen data across all risk categories.
