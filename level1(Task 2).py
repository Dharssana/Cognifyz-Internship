import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset = pd.read_csv(r"C:\Users\Kesavaraj\Downloads\cognifyz-main\cognifyz-main\Dataset .csv")

# 1. Find the city with the highest number of restaurants
city_with_highest_restaurants = dataset['City'].value_counts().idxmax()
restaurant_counts = dataset['City'].value_counts()

# 2. Calculate the average ratings for restaurants in each city
average_ratings_by_city = dataset.groupby('City')['Aggregate rating'].mean()

# 3. Find the city with the highest average rating
city_with_highest_avg_rating = average_ratings_by_city.idxmax()
highest_avg_rating = average_ratings_by_city.max()

# Print the results
print(f"The city with the highest number of restaurants is: {city_with_highest_restaurants}")
print(f"The city with the highest average rating is: {city_with_highest_avg_rating} with an average rating of {highest_avg_rating:.2f}")
print("\nAverage rating for restaurants in each city:")
print(average_ratings_by_city)

# Visualize the top 10 cities with the most restaurants
top_10_cities = restaurant_counts.head(10)
plt.figure(figsize=(10, 6))
top_10_cities.plot(kind='bar', color='skyblue')
plt.xlabel('City', fontsize=12)
plt.ylabel('Number of Restaurants', fontsize=12)
plt.title('Top 10 Cities with the Most Restaurants', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualize the average ratings for the top 10 cities
top_10_cities_avg_ratings = average_ratings_by_city[top_10_cities.index]
plt.figure(figsize=(10, 6))
top_10_cities_avg_ratings.plot(kind='bar', color='orange')
plt.xlabel('City', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.title('Average Ratings in Top 10 Cities', fontsize=14)
plt.xticks(rotation=45)
plt.ylim(0, 5)
plt.tight_layout()
plt.show()
