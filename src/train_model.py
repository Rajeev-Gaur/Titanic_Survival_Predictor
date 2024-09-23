from sklearn.naive_bayes import GaussianNB
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix

def train_and_evaluate_model(df):
    # Separate features and target variable
    X = df.drop('Survived', axis=1)
    y = df['Survived']

    # Train the model
    model = GaussianNB()
    model.fit(X, y)

    # Save the model
    joblib.dump(model, 'models/naive_bayes_titanic_model.pkl')

    # Generate predictions
    predictions = model.predict(X)

    # Classification report
    report = classification_report(y, predictions)
    with open('output/reports/classification_report.txt', 'w') as f:
        f.write(report)

    # Confusion matrix
    cm = confusion_matrix(y, predictions)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.savefig('output/figures/confusion_matrix.png')
    plt.close()  # Close the plot to avoid display

    # Optionally save predictions
    pd.DataFrame(predictions, columns=['Predicted']).to_csv('output/predictions/predictions.csv', index=False)



