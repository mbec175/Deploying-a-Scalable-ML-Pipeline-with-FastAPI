# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This project uses a Random Forest Classifier from scikit-learn to predict whether a person's annual income exceeds $50,000 based on census demographic and employment information. The model was trained using the UCI Census Income dataset. Categorical variables were processed using one-hot encoding and the target label was binarized before training. 

## Intended Use
The model is intended for educational purposes as part of a machine learning pipeline and deployment project. It demonstrates data preprocessing, model training, inference, evaluation, and API deployment using FastAPI.

The model predicts whether an individual's income is greater than $50K or less than or equal to $50K based on census features such as age, education, occupation, marital status, and hours worked per week.

## Training Data
The training data comes from the UCI Census Income dataset. The dataset contains demographic and employment-related information collected from U.S. Census data.

The dataset includes features such as:
- age
- workclass
- education
- occupation
- race
- sex
- hours-per-week
- native-country

The target variable is salary, which contains the classes:
- <=50K
- >50K

The dataset used in this project contains 32,561 rows and 15 columns.

## Evaluation Data
The dataset was split into training and testing datasets using an 80/20 train-test split with a fixed random state for reproducibility. The test dataset was used to evaluate model performance after training.

## Metrics
The model was evaluated using precision, recall, and F1 score.

Model performance:
- Precision: 0.7419
- Recall: 0.6384
- F1 Score: 0.6863

These metrics were calculated using the held-out test dataset.

## Ethical Considerations
This dataset contains demographic information such as race, sex, and native-country. Because of this, the model may reflect biases that exist in the original census data. Predictions made by the model could potentially differ across demographic groups.

This model should not be used to make real-world decisions involving employment, hiring, financial approval, or other high-impact situations. The project is intended strictly for educational and demonstration purposes.

## Caveats and Recommendations
The model performance is limited by the quality and representativeness of the dataset. Additionally, the dataset is relatively old and may not accurately reflect current economic or demographic conditions.

Future improvements could include:
- hyperparameter tuning
- cross-validation
- feature engineering
- fairness and bias analysis
- experimenting with additional machine learning models

The current implementation prioritizes simplicity and reproducibility for instructional purposes.