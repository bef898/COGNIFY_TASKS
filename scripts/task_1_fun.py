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
    def Level_1_Task4(self,data:pd.DataFrame):
        #find the required columns for the task
        required_columns = ['restaurant_id', 'has_online_delivery', 'aggregate_rating']
        for column in required_columns:
            if column not in data.columns:
                raise KeyError(f"column '{column} not found in Dataframe. ")
        #calculate percentage of resturants that has online delivery
        online_delivey_count = data['has_online_delivery'].value_counts()
        total_restaurant = data['restaurant_id'].nunique()
        online_delivery_percentage = (online_delivey_count/total_restaurant) * 100

        #calculate avg rating of resturant 
        avg_rating_with_delivery = data[data['has_online_delivery'] == 'Yes']['aggregate_rating'].mean()
        avg_rating_with_out_delivery = data[data['has_online_delivery'] == 'No']['aggregate_rating'].mean()
        return online_delivery_percentage,avg_rating_with_delivery,avg_rating_with_out_delivery

