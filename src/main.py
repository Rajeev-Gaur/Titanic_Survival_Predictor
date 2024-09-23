import os
from src.config import TRAIN_DATA
from src.preprocessing_data import load_data, preprocess_data
from src.train_model import train_and_evaluate_model

def create_output_directories():
    output_dirs = ['output/figures', 'output/reports', 'output/predictions', 'models']
    for directory in output_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)

def main():
    create_output_directories()  # Create output directories if they don't exist
    
    # Load the training data
    df = load_data(TRAIN_DATA)
    
    # Preprocess the data
    df = preprocess_data(df)
    
    # Train and evaluate the model
    train_and_evaluate_model(df)

if __name__ == "__main__":
    main()

 




