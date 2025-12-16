# 🎬 Netflix Content Library Analysis

## Project Overview
This project performs an exploratory data analysis (EDA) and visualization of the Netflix content library (over 8,800 titles). The primary goal was to uncover key trends in content distribution, growth over time, and format characteristics (Movies vs. TV Shows) using Python for data cleaning and visualization.

## Key Features & Insights

* **Content Split:** Confirmed the library is predominantly **Movies (approx. 69%)** compared to TV Shows (approx. 31%).
* **Annual Growth Trend:** Visualized the historical release data, highlighting the significant surge in content acquisition, particularly the **exponential growth in TV Show releases** in recent years.
* **Movie Duration Analysis:** Determined that the majority of Netflix movies have a duration tightly clustered between **90 and 120 minutes.**
* **Geographic Focus:** Identified the **United States** as the primary content contributor, followed by other major international markets.
* **Content Ratings:** Analyzed and charted the distribution of content ratings across the platform.

## Technical Stack
| Category | Tools & Libraries |
| :--- | :--- |
| **Language** | Python |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, `plt.subplots` |
| **Data Source** | `netflix_titles.csv` (8807 records) |

## Methodology

1.  **Data Loading:** Loaded the `netflix_titles.csv` dataset into a Pandas DataFrame.
2.  **Data Cleaning & Wrangling:**
    * Handled missing values (`NaN`) in the `rating` and `duration` columns to prevent runtime errors.
    * Extracted and converted movie duration strings (e.g., "90 min") into numerical integers for histogram plotting.
    * Grouped data by `release_year` and `type` to track historical content growth.
3.  **Visualization:** Generated six distinct visualizations using Matplotlib, ensuring appropriate data filtering for each chart.

## Visualizations

### 1. Movies vs. TV Shows on Netflix
A bar chart comparing the total count of titles by format.


### 2. Distribution of Content Ratings
A pie chart showing the percentage breakdown of content ratings.


### 3. Distribution of Movie Durations
A histogram illustrating the frequency of movie lengths in minutes.

### 4. Titles Released Per Year
A scatter plot showing the total number of titles released by year.


### 5. Top 10 Countries by Title Count
A horizontal bar chart showing the countries with the most content contributions.


### 6. Movies vs. TV Shows Released Each Year
A two-panel subplot comparing the yearly release count of movies and TV shows over time, clearly showing the divergent growth paths.


## Files in this Repository

* `capstone_netflix.py`: The final Python script containing all data cleaning and visualization code.
* `netflix_titles.csv`: The raw dataset used for the analysis.
* `output/`: Directory containing all generated PNG image files.

***
*This project was developed as a data analysis and visualization exercise.*
