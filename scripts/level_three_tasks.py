import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer

class LevelThreeTasks:
    def __init__(self, data):
        self.data = data

    def analyze_reviews(self):
        """Analyze reviews to find common positive and negative keywords and explore review length."""
        # Assuming a 'reviews' column exists in the dataset
        if 'rating_text' not in self.data.columns:
            print("No 'rating_text' column found in the dataset.")
            return None, None
        
        # Preprocess reviews and tokenize
        reviews = self.data['rating_text'].dropna()
        vectorizer = CountVectorizer(stop_words='english')
        word_counts = vectorizer.fit_transform(reviews)
        words = vectorizer.get_feature_names_out()
        word_freq = word_counts.toarray().sum(axis=0)
        word_freq_df = pd.DataFrame({'word': words, 'frequency': word_freq}).sort_values(by='frequency', ascending=False)
        
        # Positive and negative words
        top_positive = word_freq_df.head(10)
        print("Top Positive Words:")
        print(top_positive)
        
        # Average length of reviews
        self.data['review_length'] = self.data['rating_text'].fillna("").apply(len)
        avg_review_length = self.data['review_length'].mean()
        print(f"Average Review Length: {avg_review_length}")
        
        # Relationship between review length and ratings
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x='review_length', y='aggregate_rating', alpha=0.5, color='orange')
        plt.title('Review Length vs. Aggregate Rating', fontsize=16)
        plt.xlabel('Review Length', fontsize=12)
        plt.ylabel('Aggregate Rating', fontsize=12)
        plt.tight_layout()
        plt.show()
        
        return top_positive, avg_review_length

    def votes_analysis(self):
        """Analyze the highest and lowest votes and their correlation with ratings."""
        # Highest and lowest votes
        highest_votes = self.data.sort_values(by='votes', ascending=False).head(1)
        lowest_votes = self.data[self.data['votes'] > 0].sort_values(by='votes', ascending=True).head(1)
        
        print("Restaurant with Highest Votes:")
        print(highest_votes[['restaurant_name', 'votes', 'aggregate_rating']])
        print("\nRestaurant with Lowest Votes:")
        print(lowest_votes[['restaurant_name', 'votes', 'aggregate_rating']])
        
        # Correlation between votes and ratings
        correlation = self.data['votes'].corr(self.data['aggregate_rating'])
        print(f"\nCorrelation between Votes and Ratings: {correlation}")
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x='votes', y='aggregate_rating', alpha=0.5, color='blue')
        plt.title('Votes vs. Aggregate Rating', fontsize=16)
        plt.xlabel('Votes', fontsize=12)
        plt.ylabel('Aggregate Rating', fontsize=12)
        plt.tight_layout()
        plt.show()
        
        return highest_votes, lowest_votes, correlation

    def price_range_analysis(self):
        """Analyze the relationship between price range, online delivery, and table booking."""
        # Relationship between price range and services
        table_booking = self.data.groupby('price_range')['has_table_booking'].value_counts(normalize=True).unstack()
        online_delivery = self.data.groupby('price_range')['has_online_delivery'].value_counts(normalize=True).unstack()
        
        print("Table Booking Availability by Price Range:")
        print(table_booking)
        print("\nOnline Delivery Availability by Price Range:")
        print(online_delivery)
        
        # Visualization
        plt.figure(figsize=(10, 6))
        sns.heatmap(table_booking, annot=True, fmt='.2f', cmap='Blues')
        plt.title('Table Booking Availability by Price Range', fontsize=16)
        plt.xlabel('Has Table Booking', fontsize=12)
        plt.ylabel('Price Range', fontsize=12)
        plt.tight_layout()
        plt.show()
        
        plt.figure(figsize=(10, 6))
        sns.heatmap(online_delivery, annot=True, fmt='.2f', cmap='Greens')
        plt.title('Online Delivery Availability by Price Range', fontsize=16)
        plt.xlabel('Has Online Delivery', fontsize=12)
        plt.ylabel('Price Range', fontsize=12)
        plt.tight_layout()
        plt.show()
        
        return table_booking, online_delivery
