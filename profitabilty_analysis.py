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