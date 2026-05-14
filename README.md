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


Let's break down the Classification Report for the CNN model, focusing on how well it performs for each risk level:

Precision: This metric tells us, for each class, out of all the instances the model predicted as that class, how many were actually correct.

Class 0 (Low Risk): 0.87 - When the CNN predicts 'Low Risk', it is correct 87% of the time.
Class 1 (Medium Risk): 0.96 - When the CNN predicts 'Medium Risk', it is correct 96% of the time. This is very high, indicating few false positives for medium risk.
Class 2 (High Risk): 0.74 - When the CNN predicts 'High Risk', it is correct 74% of the time. This is lower than the other classes, suggesting the model sometimes misclassifies other risks as high risk.
Recall: This metric tells us, for each actual class, out of all the instances that truly belong to that class, how many did the model correctly identify.

Class 0 (Low Risk): 0.87 - The CNN correctly identifies 87% of all actual 'Low Risk' instances.
Class 1 (Medium Risk): 0.92 - The CNN correctly identifies 92% of all actual 'Medium Risk' instances.
Class 2 (High Risk): 0.96 - The CNN correctly identifies 96% of all actual 'High Risk' instances. This is a very strong recall, meaning the model is excellent at catching actual high-risk cases, even if it sometimes mislabels other cases as high risk (as seen in the lower precision).
F1-Score: The F1-Score is a balanced measure, the harmonic mean of precision and recall. It's especially useful when classes are imbalanced (which we addressed with SMOTE).

Class 0 (Low Risk): 0.87
Class 1 (Medium Risk): 0.94
Class 2 (High Risk): 0.83
Support: This is the actual number of occurrences of each class in your test dataset.

Class 0 (Low Risk): 140
Class 1 (Medium Risk): 596
Class 2 (High Risk): 78
Accuracy: This is the overall proportion of correct predictions across all classes. The CNN achieved an overall accuracy of 0.92 (92%) on the test set.

Macro Avg: This is the average of precision, recall, and F1-score across all classes, treating each class equally. It gives an idea of the model's performance on a per-class basis, without considering class imbalance. For the CNN, the Macro Avg F1-Score is 0.88.

Weighted Avg: This is the average of precision, recall, and F1-score, weighted by the number of instances in each class (support). This reflects the overall performance more accurately when classes are imbalanced.

The Weighted Avg F1-Score for the CNN is 0.92.
In summary, the CNN model demonstrates strong overall performance with 92% accuracy. It excels at identifying actual 'High Risk' cases (high recall for class 2) but has some room for improvement in its precision for that class. For 'Medium Risk', it shows consistently high performance across all metrics. The 'Low Risk' class also performs well, indicating a robust model overall.



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

<img width="690" height="307" alt="image" src="https://github.com/user-attachments/assets/a0dbf4d5-f3f1-4933-a012-99cf8fac99c8" />
<img width="768" height="627" alt="image" src="https://github.com/user-attachments/assets/3292394b-cd57-47e5-848a-c000885a68e1" />

<img width="1048" height="592" alt="image" src="https://github.com/user-attachments/assets/4090f432-3f7e-4434-809a-998c029e097c" />


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


**COMPARING THE CNN TO RF**

Let's compare the performance metrics of the Random Forest and CNN models based on their classification reports.

Overall Accuracy:

Random Forest: Achieved an accuracy of 0.95 (95%).
CNN: Achieved an accuracy of 0.92 (92%).
Precision, Recall, and F1-score by Class:

Class 0 (Low Risk):

Random Forest: Precision: 0.89, Recall: 0.94, F1-score: 0.92
CNN: Precision: 0.87, Recall: 0.87, F1-score: 0.87
Comparison: Random Forest shows slightly better precision and recall for 'Low Risk' cases.
Class 1 (Medium Risk):

Random Forest: Precision: 0.97, Recall: 0.96, F1-score: 0.96
CNN: Precision: 0.96, Recall: 0.92, F1-score: 0.94
Comparison: Random Forest has a marginal edge in precision and recall for 'Medium Risk', though both models perform exceptionally well here.
Class 2 (High Risk):

Random Forest: Precision: 0.88, Recall: 0.86, F1-score: 0.87
CNN: Precision: 0.74, Recall: 0.96, F1-score: 0.83
Comparison: This is where the models show the most significant difference.
The Random Forest has a higher precision for 'High Risk' (0.88 vs 0.74), meaning when it predicts 'High Risk', it's more often correct than the CNN.
The CNN has a notably higher recall for 'High Risk' (0.96 vs 0.86), indicating it is much better at identifying all actual 'High Risk' instances, even if it sometimes misclassifies other risks as high (leading to lower precision).
Macro Average F1-Score (unweighted average across classes):

Random Forest: 0.92
CNN: 0.88
Weighted Average F1-Score (weighted by support for each class):

Random Forest: 0.95
CNN: 0.92
Summary and Conclusion:

Random Forest generally exhibits slightly superior overall performance, as evidenced by its higher accuracy (95% vs 92%) and weighted average F1-score (0.95 vs 0.92). It maintains a strong balance between precision and recall across all classes.
The CNN model shows a unique strength in its recall for 'High Risk' (0.96), suggesting it is highly effective at identifying the majority of actual high-risk situations. However, this comes at the cost of lower precision for this class, meaning it tends to have more false positives for 'High Risk' predictions.
Depending on the specific priorities of the application (e.g., minimizing false negatives for high-risk situations vs. minimizing false positives), one model might be preferred over the other. If identifying all high-risk cases is paramount, even if it means some false alarms, the CNN's high recall for 'High Risk' is a significant advantage. If overall accuracy and balanced performance across all metrics are more critical, the Random Forest model appears to be the stronger choice.

