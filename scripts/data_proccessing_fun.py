import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, Normalizer
from sklearn.impute import SimpleImputer

class data_pro:
    def drop_duplicate(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        data.drop_duplicates(inplace=True)

        return data
 
    def missing_values(self, data: pd.DataFrame) -> float:
        """
        calculate  missing values from dataframe
        """
        missingCount = data.isnull().sum()
        
        return missingCount

    def get_numerical_columns(self, data: pd.DataFrame) -> list:
        """
        get numerical columns
        """
        return data.select_dtypes(include=['number']).columns.to_list()

    def get_categorical_columns(self, data: pd.DataFrame) -> list:
        """
        get categorical columns
        """
        return  data.select_dtypes(include=['object','datetime64[ns]']).columns.to_list()
    def standardize_column_names(self, data: pd.DataFrame):
        """Standardize column names for consistency."""
        data.columns = [col.strip().replace(' ', '_').lower() for col in data.columns]
        return data