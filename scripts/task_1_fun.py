import pandas as pd
import matplotlib.pyplot as plt

class task:
    def Level_1_Tasks_Tops(self, data: pd.DataFrame,column ,top_n = 3) -> pd.DataFrame:
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
    def Level_1_Task3_tops(self, data: pd.DataFrame, column: str = 'price_range') -> pd.DataFrame:
        # Check if the column exists in the DataFrame
        if column not in data.columns:
            raise KeyError(f"Column '{column}' not found in DataFrame.")

        # Calculate the percentage of restaurants in each price range category
        price_range_counts = data[column].value_counts()
        total_restaurants = data['restaurant_id'].nunique()
        price_range_percentage = (price_range_counts / total_restaurants) * 100

        # Create a bar chart to visualize the distribution of price ranges
        plt.figure(figsize=(10, 6))
        price_range_counts.plot(kind='bar')
        plt.title('Price Range Distribution')
        plt.xlabel('Price Range')
        plt.ylabel('Number of Restaurants')
        plt.show()

        return price_range_counts, price_range_percentage

