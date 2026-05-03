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