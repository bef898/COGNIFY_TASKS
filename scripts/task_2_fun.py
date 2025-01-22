import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point

class LevelTwoTasks:
    def __init__(self, data):
        self.data = data

    def analyze_ratings(self):
        """Analyze the distribution of ratings and calculate statistics."""
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['aggregate_rating'], bins=10, kde=True, color='skyblue')
        plt.title('Distribution of Aggregate Ratings', fontsize=16)
        plt.xlabel('Aggregate Rating', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.tight_layout()
        plt.show()
        
        # Most common rating range
        most_common_rating_range = self.data['aggregate_rating'].mode()[0]
        print(f"Most Common Rating Range: {most_common_rating_range}")
        
        # Average number of votes
        avg_votes = self.data['votes'].mean()
        print(f"Average Number of Votes: {avg_votes}")
        
        return most_common_rating_range, avg_votes

    def cuisine_combinations(self):
        """Analyze the most common combinations of cuisines and their average ratings."""
        self.data['cuisines_split'] = self.data['cuisines'].str.split(', ')
        exploded_cuisines = self.data.explode('cuisines_split')
        
        # Count the most common cuisine combinations
        cuisine_counts = exploded_cuisines['cuisines_split'].value_counts().head(10)
        print("Top 10 Most Common Cuisines:")
        print(cuisine_counts)
        
        # Analyze average ratings for each cuisine
        avg_ratings = exploded_cuisines.groupby('cuisines_split')['aggregate_rating'].mean().sort_values(ascending=False)
        print("\nAverage Ratings for Each Cuisine:")
        print(avg_ratings.head(10))
        
        return cuisine_counts, avg_ratings

    def geographic_analysis(self):
        """Plot geographic locations of restaurants and analyze clusters."""
        geometry = [Point(xy) for xy in zip(self.data['longitude'], self.data['latitude'])]
        geo_df = gpd.GeoDataFrame(self.data, geometry=geometry)
        
        # Plot the locations
        plt.figure(figsize=(10, 10))
        geo_df.plot(marker='o', color='red', markersize=5, alpha=0.5)
        plt.title('Restaurant Locations', fontsize=16)
        plt.xlabel('Longitude', fontsize=12)
        plt.ylabel('Latitude', fontsize=12)
        plt.tight_layout()
        plt.show()
        
        return geo_df

    def restaurant_chains(self):
        """Identify and analyze restaurant chains."""
        chain_counts = self.data['restaurant_name'].value_counts()
        restaurant_chains = chain_counts[chain_counts > 1]
        print("Top Restaurant Chains:")
        print(restaurant_chains.head(10))
        
        chain_ratings = self.data[self.data['restaurant_name'].isin(restaurant_chains.index)].groupby('restaurant_name')['aggregate_rating'].mean().sort_values(ascending=False)
        print("\nRatings for Popular Restaurant Chains:")
        print(chain_ratings.head(10))
        
        return restaurant_chains, chain_ratings
