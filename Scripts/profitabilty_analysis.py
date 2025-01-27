import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

merged_df = pd.read_csv('merged_dataset.csv')


profitable_products = merged_df.groupby('Product Name')['Profit'].sum().reset_index().sort_values(by='Profit', ascending=False)

profitable_categories = merged_df.groupby('Category')['Profit'].sum().reset_index().sort_values(by='Profit', ascending=False)

profitable_regions = merged_df.groupby('Country')['Profit'].sum().reset_index().sort_values(by='Profit', ascending=False)

profitable_products.to_csv('profitable_products.csv', index=False)
profitable_categories.to_csv('profitable_categories.csv', index=False)
profitable_regions.to_csv('profitable_regions.csv', index=False)

print(f"Most Profitable Products: {profitable_products.head()}")
print(f"Most Profitable Categories: {profitable_categories.head()}")
print(f"Most Profitable Regions: {profitable_regions.head()}")

# Horizontal Bar Chart for Profitable Categories
plt.figure(figsize=(10, 6))
sns.barplot(data=profitable_categories, y="Category", x="Profit", palette="viridis")
plt.title("Profitable Categories", fontsize=16)
plt.xlabel("Profit ($)", fontsize=12)
plt.ylabel("Category", fontsize=12)
plt.tight_layout()
plt.savefig('profitable_categories_chart.png')
plt.show()

#vertical bar chart for the top 10 profitable regions
top_regions = profitable_regions.sort_values(by="Profit", ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_regions, x="Country", y="Profit", palette="coolwarm")
plt.title("Top 10 Profitable Regions", fontsize=16)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Profit ($)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig('profitable_regions_chart.png')
plt.show()
