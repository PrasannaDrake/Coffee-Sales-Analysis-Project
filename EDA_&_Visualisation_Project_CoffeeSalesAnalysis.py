import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings('ignore')

# ================================
# Load the Dataset
# ================================
data = pd.read_csv("index.csv")

# ================================
# Basic Data Inspection
# ================================
print(data.head())
print(data.info())
print(data.describe())
print("Missing Values:\n", data.isnull().sum())
print("Duplicate Rows:", data.duplicated().sum())

# ================================
# Data Cleaning
# ================================

# Convert date columns to datetime
data['date'] = pd.to_datetime(data['date'])
data['datetime'] = pd.to_datetime(data['datetime'])

# Create new time-based features
data['month'] = data['date'].dt.strftime('%Y-%m')
data['day'] = data['date'].dt.strftime('%w')  # 0 = Sunday, 6 = Saturday
data['hour'] = data['datetime'].dt.strftime('%H')

# Check 'card' nulls
print(data[data['card'].isnull()]['cash_type'].value_counts())

# ================================
# Exploratory Data Analysis (EDA)
# ================================

# Overall revenue by product
revenue_data = data.groupby('coffee_name').sum(numeric_only=True).reset_index().sort_values(by='money', ascending=False)
plt.figure(figsize=(10, 4))
ax = sns.barplot(data=revenue_data, x='money', y='coffee_name', color='steelblue')
ax.bar_label(ax.containers[0], fontsize=6)
plt.title('Revenue by Coffee Type')
plt.xlabel('Revenue')
plt.ylabel('Coffee Name')
plt.show()

# Monthly sales count by product
monthly_sales = (
    data.groupby(['coffee_name', 'month'])
    .count()['date']
    .reset_index()
    .rename(columns={'date': 'count'})
    .pivot(index='month', columns='coffee_name', values='count')
    .reset_index()
)
monthly_sales = monthly_sales.fillna(0)
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales)
plt.xticks(range(len(monthly_sales['month'])), monthly_sales['month'])
plt.title("Monthly Coffee Sales by Type")
plt.xlabel("Month")
plt.ylabel("Number of Sales")
plt.legend(title='Coffee Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Sales by day of the week
weekday_sales = data.groupby('day').count()['date'].reset_index().rename(columns={'date': 'count'})
plt.figure(figsize=(10, 6))
sns.barplot(data=weekday_sales, x='day', y='count', color='steelblue')
plt.xticks(range(7), ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
plt.title("Sales Distribution Over Weekdays")
plt.xlabel("Day")
plt.ylabel("Number of Sales")
plt.show()

# Hourly sales pattern
hourly_sales = data.groupby('hour').count()['date'].reset_index().rename(columns={'date': 'count'})
plt.figure(figsize=(14, 6))
sns.barplot(data=hourly_sales, x='hour', y='count', color='steelblue')
plt.title("Sales by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Sales")
plt.show()

# Hourly sales by coffee type
hourly_sales_by_coffee = (
    data.groupby(['hour', 'coffee_name'])
    .count()['date']
    .reset_index()
    .rename(columns={'date': 'count'})
    .pivot(index='hour', columns='coffee_name', values='count')
    .fillna(0)
    .reset_index()
)

# Plot hourly trend for each coffee type
fig, axs = plt.subplots(2, 4, figsize=(20, 10))
axs = axs.flatten()
for i, coffee_type in enumerate(hourly_sales_by_coffee.columns[1:]):
    axs[i].bar(hourly_sales_by_coffee['hour'], hourly_sales_by_coffee[coffee_type])
    axs[i].set_title(coffee_type)
    axs[i].set_xlabel("Hour")
    axs[i].set_ylabel("Sales")
plt.tight_layout()
plt.show()
