import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns


merged_df = pd.read_csv('merged_dataset.csv')

#sales & profits by country
country_metrics = merged_df.groupby('Country').agg(
    total_sales=('Sales', 'sum'),
    total_profit=('Profit', 'sum')
).reset_index().sort_values(by='total_sales', ascending=False)

#product demand by country & city
product_demand = merged_df.groupby(['Country', 'City', 'Product Name']).agg(
    total_sales=('Sales', 'sum'),
    product_count=('Product.ID', 'count')
).reset_index().sort_values(by='total_sales', ascending=False)

#country_metrics.to_csv('country_metrics.csv', index=False)
#product_demand.to_csv('product_demand.csv', index=False)

print(f"Sales & Profits by Country: \n{country_metrics.head()}")
print(f"Product Demand: \n{product_demand.head()}")


#sales & profits by Country
plt.figure(figsize=(12, 6))
sns.barplot(data=country_metrics.head(10), x='Country', y='total_sales', color='blue', label='Total Sales')
sns.barplot(data=country_metrics.head(10), x='Country', y='total_profit', color='orange', label='Total Profit')
plt.title('Top 10 Countries by Sales and Profit')
plt.ylabel('Amount')
plt.xticks(rotation=45)
plt.legend()
# Format y-axis in millions
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e6:.1f}M'))
plt.tight_layout()
plt.savefig('country_metrics_visualization.png')
plt.show()


#product demand (Top 10 Cities)
top_cities_products = product_demand.groupby(['City', 'Product Name']).agg(
    total_sales=('total_sales', 'sum')
).reset_index().sort_values(by='total_sales', ascending=False)

top_cities_products = top_cities_products.groupby('City').head(1).reset_index().head(10)

plt.figure(figsize=(14, 7))
sns.barplot(data=top_cities_products, x='City', y='total_sales', hue='Product Name', dodge=False, palette='viridis')

plt.title('Top 10 Cities by Product Demand with Products')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend(title='Product Name', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig('product_demand_by_city_and_product.png')
plt.show()