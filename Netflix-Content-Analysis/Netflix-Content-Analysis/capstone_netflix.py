import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
df = pd.read_csv('netflix_titles.csv')

#clean the dataset
df.dropna(subset=['release_year', 'type'], inplace=True)

types_count = df['type'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(types_count.index, types_count.values, color=['red', 'blue'])
plt.title('Number of Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(10, 6))
plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Content Ratings on Netflix')
plt.tight_layout()
plt.savefig('content_ratings_distribution.png')
plt.show()

# ... (rest of the code for the first two visualizations)

movie_df = df[df['type'] == 'Movie'].copy()

# ---> CRITICAL CORRECTION IS HERE <---
# Drop rows with missing 'duration' before attempting string conversion
movie_df.dropna(subset=['duration'], inplace=True) 

# Now this line is safe, as all 'duration' values are non-null strings
movie_df['duration_int'] = movie_df['duration'].str.replace(' min', '', regex=False).astype(int)

# ... (rest of the plotting code)
plt.figure(figsize=(10, 6))
plt.hist(movie_df['duration_int'], bins=30, color='green', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movie_durations_distribution.png')
plt.show()


release_year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.scatter(release_year_counts.index, release_year_counts.values, color='purple')
plt.title('Number of Titles Released Each Year on Netflix')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.savefig('titles_released_per_year.png')
plt.show()


country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.barh(country_counts.index, country_counts.values, color='orange')
plt.title('Top 10 Countries by Number of Titles on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top_countries_by_titles.png')
plt.show()

content_by_year = df.groupby('release_year')['type'].value_counts().unstack().fillna(0)

fig,ax=plt.subplots(2,1,figsize=(12,6))

#first subplot for Movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='red')
ax[0].set_title('Number of Movies Released Each Year on Netflix')
ax[0].set_xlabel('Release Year')
ax[0].set_ylabel('Number of Movies')

#second subplot for TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='blue')
ax[1].set_title('Number of TV Shows Released Each Year on Netflix')     
ax[1].set_xlabel('Release Year')
ax[1].set_ylabel('Number of TV Shows')


fig.suptitle('Movies vs TV Shows Released Each Year on Netflix', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('movies_vs_tvshows_per_year.png')
plt.show()