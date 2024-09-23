# Titanic Survival Predictor

## Project Overview

The Titanic Survival Predictor is a machine learning project aimed at predicting whether a passenger survived the Titanic disaster based on various features, including age, gender, class, and embarkation point. This project utilizes the Naive Bayes algorithm for classification.

## Table of Contents

- [Project Overview]
- [Dataset]
- [Installation]
- [Usage]
- [Exploratory Data Analysis]
- [Model Evaluation]
- [Future Enhancements]
- [Contributing]
- [License]

## Dataset

The dataset used for this project consists of three files from the Kaggle Titanic competition:

1. **train.csv**: The training dataset used for building the model. It contains information about passengers, including survival status.
2. **test.csv**: The testing dataset used to evaluate the model's performance.
3. **gender_submission.csv**: A sample submission file that shows the format for submitting predictions.


### Features in the Dataset:
- **PassengerId**: Unique identifier for each passenger
- **Survived**: Survival status (0 = No, 1 = Yes)
- **Pclass**: Ticket class (1st, 2nd, 3rd)
- **Name**: Name of the passenger
- **Sex**: Gender of the passenger
- **Age**: Age in years
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Ticket**: Ticket number
- **Fare**: Fare paid for the ticket
- **Cabin**: Cabin number
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

## Installation

To set up the project environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/rajeev-gaur/Titanic_Survival_Predictor.git
   cd Titanic_Survival_Predictor


Install the required packages:
pip install -r requirements.txt


Usage
To run the project, execute the following command:
python src/main.py
This will preprocess the data, train the Naive Bayes model, and evaluate its performance on the test set. The trained model will be saved in the models/ directory.

Exploratory Data Analysis
In the notebooks/titanic_analysis.ipynb file, you can explore various visualizations and analyses of the Titanic dataset, including:

Survival rates by gender and class
Age distribution of passengers
Correlation heatmaps of features


Model Evaluation
The model's performance is evaluated using accuracy, confusion matrix, and classification report, which are printed to the console upon running the model training script.

Future Enhancements
Feature engineering to create additional relevant features.
Hyperparameter tuning to optimize the Naive Bayes model.
Implementing other classification algorithms for comparison.
Cross-validation for a more robust evaluation of model performance.


License
This project is licensed under the MIT License - see the LICENSE file for details.