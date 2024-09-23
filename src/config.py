import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data paths
DATA_PATH = os.path.join(BASE_DIR, 'data/')
TRAIN_DATA = os.path.join(DATA_PATH, 'train.csv')
TEST_DATA = os.path.join(DATA_PATH, 'test.csv')
SUBMISSION_DATA = os.path.join(DATA_PATH, 'gender_submission.csv')

# Add any other configuration settings here as needed
