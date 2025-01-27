import pandas as pd
import matplotlib.pyplot as plt


merged_df = pd.read_csv('merged_dataset.csv')

# avg profitability by shipping mode
shipping_profitability = merged_df.groupby('Ship.Mode').agg(
    avg_shipping_cost=('Shipping.Cost', 'mean'),
    total_profit=('Profit', 'sum')
).reset_index().sort_values(by='total_profit', ascending=False)

shipping_profitability.to_csv('shipping_profitability.csv', index=False)
print(f"Shipping Profitability: {shipping_profitability}")

# bar chart with 2 axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# bar chart for avg shipping cost
ax1.bar(
    shipping_profitability['Ship.Mode'],
    shipping_profitability['avg_shipping_cost'],
    color='skyblue',
    label='Avg Shipping Cost'
)
ax1.set_xlabel('Shipping Mode')
ax1.set_ylabel('Avg Shipping Cost ($)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_title('Shipping Mode Analysis: Cost vs Profit')

# line chart for total profits
ax2 = ax1.twinx()
ax2.plot(
    shipping_profitability['Ship.Mode'],
    shipping_profitability['total_profit'],
    color='red',
    marker='o',
    label='Total Profit'
)
ax2.set_ylabel('Total Profit ($)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
ax1.grid(visible=True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('shipping_profitability_analysis.png')
plt.show()