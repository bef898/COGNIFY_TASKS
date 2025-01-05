import pandas as pd

class task:
    def Task_1_Tops(self, data: pd.DataFrame,column ,top_n = 3) -> pd.DataFrame:
        # Check if the column exists in the DataFrame
        if column not in data.columns:
            raise KeyError(f"Column '{column}' not found in DataFrame.")

        value_split = data[column].dropna().str.split(', ').explode()

        #top value
        top_values = value_split.value_counts().head(top_n)

        #calculate percantage of occurence for each value
        top_resturant = data['restaurant_id'].nunique()
        top_values_percentage = (top_values/top_resturant) * 100
        return top_values,top_values_percentage

