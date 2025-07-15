# ☕ Coffee Sales Analysis — EDA & Visualization

This project focuses on **exploratory data analysis (EDA)** of a coffee vending machine dataset, aiming to understand **customer behavior**, **sales trends**, and **product performance** using Python.

---

## 📌 Project Overview

The dataset includes transaction records from a coffee vending machine between **March 2024 and July 2024**. By analyzing the data, we aim to:

- Uncover **top-performing coffee products**
- Identify **peak sales hours and weekdays**
- Evaluate **payment method preferences**
- Generate **monthly sales patterns**
- Support **inventory and restocking decisions**

---

## 🧰 Tools & Libraries

- **Python 3.8+**
- `pandas` – data manipulation
- `numpy` – numerical analysis
- `matplotlib`, `seaborn` – visualizations
- `datetime`, `warnings` – data formatting & cleanup

---

## 📂 Dataset Details

- 📄 **File**: `index.csv`
- 📆 **Timeframe**: March 2024 – July 2024
- 🔢 **Records**: 1,133 transactions
- 🧾 **Fields**:
  - `date` – transaction date
  - `datetime` – full timestamp
  - `cash_type` – payment type (cash/card)
  - `card` – anonymized card ID (nullable for cash)
  - `money` – amount spent
  - `coffee_name` – name of the coffee purchased

---

## 📊 Key Insights

- **Most popular products**: Americano with Milk, Latte
- **Top revenue generator**: Latte
- **Peak hours**: 10:00 AM & 7:00 PM
- **Highest weekday sales**: Tuesday
- **92% of transactions** use card payments

---

## 📈 Visualizations Included

- Revenue by coffee type
- Monthly sales trends
- Hourly and weekday sales breakdown
- Product-wise hourly demand
- Coffee type popularity chart

---

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/coffee-sales-analysis.git
   cd coffee-sales-analysis
