import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load the dataset
file_path = r'C:\Users\Kesavaraj\Downloads\cognifyz-main\cognifyz-main\Dataset .csv'
df = pd.read_csv(file_path)

# Simulate 'Reviews' using the 'Rating text' column (if actual reviews are unavailable)
df['Reviews'] = df['Rating text']

# Define a custom stopwords list
custom_stopwords = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your',
    'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her',
    'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs',
    'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those',
    'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
    'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
    'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with',
    'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
    'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
    'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
    'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
    'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
    'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
}

# Clean and tokenize the reviews
df['Cleaned Reviews'] = df['Reviews'].str.lower().str.replace(r'[^\w\s]', '', regex=True)
df['Tokenized Reviews'] = df['Cleaned Reviews'].apply(
    lambda x: [word for word in str(x).split() if word not in custom_stopwords]
)

# Flatten tokenized words to a single list
all_words = [word for review in df['Tokenized Reviews'] for word in review]

# Define positive and negative keywords
positive_words = {'good', 'great', 'excellent', 'amazing', 'delicious', 'perfect', 'love'}
negative_words = {'bad', 'poor', 'terrible', 'awful', 'horrible', 'disappointing', 'worst'}

# Count occurrences of positive and negative words
word_counts = Counter(all_words)
most_common_positive = {word: count for word, count in word_counts.items() if word in positive_words}
most_common_negative = {word: count for word, count in word_counts.items() if word in negative_words}

# Calculate the average length of reviews
df['Review Length'] = df['Cleaned Reviews'].apply(lambda x: len(str(x).split()))
average_review_length = df['Review Length'].mean()

# Explore the relationship between review length and rating
correlation = df['Review Length'].corr(df['Aggregate rating'])

# Display the results
print("Most Common Positive Keywords:", most_common_positive)
print("Most Common Negative Keywords:", most_common_negative)
print(f"Average Review Length: {average_review_length:.2f} words")
print(f"Correlation Between Review Length and Rating: {correlation:.2f}")

# Visualize the relationship between review length and aggregate rating
plt.figure(figsize=(8, 5))
plt.scatter(df['Review Length'], df['Aggregate rating'], alpha=0.6, color='blue')
plt.title('Relationship Between Review Length and Aggregate Rating')
plt.xlabel('Review Length (words)')
plt.ylabel('Aggregate Rating')
plt.grid(True)
plt.show()
