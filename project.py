import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# Ensure plots show in VS Code
matplotlib.use('TkAgg')

# --- GLOBAL STYLE ---
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (9,6)

print("Project Started")

# --- LOAD DATA ---
df = pd.read_csv("zomato.csv")

# Normalize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Rename long column
df.rename(columns={'approx_cost(for_two_people)': 'cost_for_two'}, inplace=True)

# --- CLEAN RATE COLUMN ---
df['rate'] = df['rate'].astype(str)
df['rate'] = df['rate'].replace(['NEW', '-', 'nan'], None)
df['rate'] = df['rate'].str.replace('/5', '', regex=False)
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

# --- CLEAN COST COLUMN (IMPORTANT FIX) ---
df['cost_for_two'] = df['cost_for_two'].astype(str)
df['cost_for_two'] = df['cost_for_two'].str.replace(',', '')  # remove commas
df['cost_for_two'] = pd.to_numeric(df['cost_for_two'], errors='coerce')

# Drop only necessary nulls
df.dropna(subset=['rate', 'location', 'cuisines', 'cost_for_two'], inplace=True)

print("Cleaned Data Shape:", df.shape)

# --- ANALYSIS ---
top_locations = df['location'].value_counts().head(10)
top_cuisines = df['cuisines'].value_counts().head(10)

print("\nTop Locations:\n", top_locations)
print("\nTop Cuisines:\n", top_cuisines)
print("\nRating Summary:\n", df['rate'].describe())

# --- VISUALIZATION ---

# 🔹 1. Top Locations
plt.figure()
colors = sns.color_palette("Blues_r", len(top_locations))
sns.barplot(x=top_locations.values, y=top_locations.index, palette=colors)

plt.title("Top 10 Locations with Most Restaurants", fontsize=14, weight='bold')
plt.xlabel("Number of Restaurants")
plt.ylabel("Location")

plt.savefig("top_locations.png", dpi=300, bbox_inches='tight')
plt.show()

print("Insight: BTM, HSR, and Koramangala have highest restaurant density.\n")


# 🔹 2. Top Cuisines
plt.figure()
colors = sns.color_palette("magma", len(top_cuisines))
sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette=colors)

plt.title("Top 10 Cuisines", fontsize=14, weight='bold')
plt.xlabel("Count")
plt.ylabel("Cuisine")

plt.savefig("top_cuisines.png", dpi=300, bbox_inches='tight')
plt.show()

print("Insight: North Indian and Chinese cuisines dominate demand.\n")


# 🔹 3. Ratings Distribution
plt.figure()
sns.histplot(df['rate'], bins=20, kde=True, color="#2ecc71")

plt.title("Distribution of Ratings", fontsize=14, weight='bold')
plt.xlabel("Rating")
plt.ylabel("Frequency")

plt.savefig("ratings_distribution.png", dpi=300, bbox_inches='tight')
plt.show()

print("Insight: Ratings mostly lie between 3.5–4.2.\n")


# 🔹 4. Cost vs Rating (FIXED AXIS ISSUE)
plt.figure()
sns.scatterplot(
    x=df['cost_for_two'],
    y=df['rate'],
    hue=df['rate'],
    palette="viridis"
)

plt.title("Cost vs Rating", fontsize=14, weight='bold')
plt.xlabel("Cost for Two")
plt.ylabel("Rating")

# FIX CLUTTER
plt.locator_params(axis='x', nbins=10)
plt.xticks(rotation=30)

plt.savefig("cost_vs_rating.png", dpi=300, bbox_inches='tight')
plt.show()

print("Insight: Higher cost does not guarantee better ratings.\n")


# 🔹 5. Boxplot
plt.figure()
sns.boxplot(x=df['rate'], color="#3498db")

plt.title("Boxplot of Ratings", fontsize=14, weight='bold')

plt.savefig("boxplot.png", dpi=300, bbox_inches='tight')
plt.show()

print("Insight: Ratings are concentrated with few outliers.\n")


# 🔹 6. Heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap", fontsize=14, weight='bold')

plt.savefig("heatmap.png", dpi=300, bbox_inches='tight')
plt.show()

print("Insight: Weak correlation between cost and rating.\n")


# --- SAVE CLEAN DATA ---
df.to_csv("clean_zomato.csv", index=False)

print("Project Completed Successfully")