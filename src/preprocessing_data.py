import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """Preprocess the DataFrame."""
    
    # Fill missing 'Age' values with the median
    df['Age'].fillna(df['Age'].median(), inplace=True)
    
    # Fill missing 'Fare' values with the median
    df['Fare'].fillna(df['Fare'].median(), inplace=True)
    
    # Convert 'Sex' to numerical values
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    
    # Fill missing 'Embarked' values with the most common port
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    
    # Convert 'Embarked' to numerical values
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)  # One-hot encoding
    
    # Drop unnecessary columns
    df.drop(columns=['Name', 'Ticket', 'Cabin'], inplace=True)
    
    return df


