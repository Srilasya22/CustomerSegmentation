"""
This is a boilerplate pipeline 'DataPreprocessing'
generated using Kedro 0.19.1
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging

def preprocess(raw):
    '''
        This function cleans the data by performing categorical encoding, feature scaling
        Args: raw data in csv format
        Returns: cleaned data frame, resampled train data, resampled test data
    '''
    try:
        df = pd.DataFrame(raw)
        df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})  # Converting categorical column to numerical column
        scaler = StandardScaler()
        scaled1_data = scaler.fit_transform(df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']])
        scaled_data=pd.DataFrame(scaled1_data)
        return df, scaled_data
    except Exception as e:
        logging.error(f"Error occurred in data preprocessing: {e}")
        raise e
