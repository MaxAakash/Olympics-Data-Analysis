import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load file in local Python environment (replace with correct path if needed)
df = pd.read_csv('olympics_data.csv', encoding='ISO-8859-1')

# Basic inspection
print(df.head())
print(df.info())
print(df.describe())

# Check and drop missing values
print("Missing Values:\n", df.isnull().sum())
df_cleaned = df.dropna()
print(df_cleaned.info())

# Top 10 Countries by Medal Count
medals_by_country = df_cleaned.groupby('Country')['Medal'].count().sort_values(ascending=False)
fig = px.bar(
    x=medals_by_country.head(10).index,
    y=medals_by_country.head(10).values,
    labels={'x': 'Country', 'y': 'Total Medals'},
    title='Top 10 Countries by Medal Count',
    color=medals_by_country.head(10).values
)
fig.show()

# Medals Won Over the Years
medals_over_years = df_cleaned.groupby('Year')['Medal'].count()
fig = px.line(
    x=medals_over_years.index,
    y=medals_over_years.values,
    labels={'x': 'Year', 'y': 'Total Medals'},
    title='Medals Won Over the Years',
    markers=True
)
fig.show()

# Gender Distribution
gender_distribution = df_cleaned['Gender'].value_counts()
fig = px.pie(
    names=gender_distribution.index,
    values=gender_distribution.values,
    title='Gender Distribution in Olympic Events'
)
fig.show()

# Top 10 Athletes by Medal Count
athlete_medal_count = df_cleaned.groupby('Athlete')['Medal'].count().sort_values(ascending=False)
fig = px.bar(
    x=athlete_medal_count.head(10).values,
    y=athlete_medal_count.head(10).index,
    orientation='h',
    title='Top 10 Athletes by Medal Count'
)
fig.show()
