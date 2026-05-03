import pandas as pd
df = pd.read_csv("zomato.csv")
print(df.head()
  
print(df.info())
print(df.columns)  

df.columns = df.columns.str.lower().str.replace(' ', '_')
print(df.isnull().sum())
df.dropna(inplace=True)

df['rate'] = df['rate'].str.replace('/5', '')
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')
print(df['location'].value_counts().head())
print(df['cuisines'].value_counts().head())
print(df['rate'].describe())

df.to_csv("clean_zomato.csv", index=False)
print(df.info())
print(df.columns)

df.columns = df.columns.str.lower().str.replace(' ', '_')
print(df.columns)
print(df.isnull().sum())

df.dropna(inplace=True)
print(df.isnull().sum())

df = df[df['rate'] != 'NEW']
df = df[df['rate'] != '-']
df['rate'] = df['rate'].str.replace('/5', '')
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')
print(df['rate'].head())
print(df['rate'].dtype)
print(df['location'].value_counts().head(10))
print(df['cuisines'].value_counts().head(10))
print(df['rate'].describe())

import matplotlib.pyplot as plt
import seaborn as sns

top_locations = df['location'].value_counts().head(10)

plt.figure()
top_locations.plot(kind='bar')
plt.title("Top 10 Locations with Most Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
sns.histplot(df['rate'], bins=20)
plt.title("Distribution of Ratings")
plt.show()

plt.figure()
sns.scatterplot(x=df['approx_cost(for_two_people)'], y=df['rate'])
plt.title("Cost vs Rating")
plt.show()