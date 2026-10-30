import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
asr = pd.read_csv("Amazon Sale Report.csv", low_memory=False)
print(asr.shape)
asr.info()

# Cleaning
asr.dropna(subset=['Order ID'], inplace=True)
asr.drop_duplicates(inplace=True)
asr['Date'] = pd.to_datetime(asr['Date'], format='%m-%d-%y')
asr['Month'] = asr['Date'].dt.month

# Analysis
total_sales = np.sum(asr['Amount'])
avg_sales = np.mean(asr['Amount'])
print("Total sales:", total_sales)
print("Average sales:", avg_sales)

# Sales by category
asr.groupby('Category')['Amount'].sum().plot(kind='bar')
plt.title('Sales by Category')
plt.show()

# Monthly trend
asr.groupby('Month')['Amount'].sum().plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.show()

# Top 10 states
asr.groupby('ship-state')['Amount'].sum().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title('Top States')
plt.show()

# Order status
asr['Status'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Order Status')
plt.show()
