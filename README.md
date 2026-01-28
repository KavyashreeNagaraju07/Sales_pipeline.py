📊 Sales Data Analysis with Python (Pandas)

This project demonstrates a simple, end-to-end data analysis pipeline using Python and Pandas.
It loads sales data from a CSV file, calculates total revenue per product, filters high-value transactions, and prints a clean summary report.

The script is plug-and-play — it automatically generates sample data, so no manual setup is required.

🚀 Features

Automatically creates a sample sales_data.csv

Loads and processes sales data using Pandas

Calculates Total Revenue per product

Filters high-value transactions (revenue > $1000)

Prints a formatted business summary report

Beginner-friendly, readable, and reusable function design

🗂️ Project Structure
.
├── sales_data.csv        # Auto-generated sample dataset
├── analysis.py           # Main analysis script
└── README.md             # Project documentation

🧠 Business Logic

Total Revenue is calculated as:

Total_Revenue = Price × Units_Sold


High-Value Sales are defined as products where:

Total_Revenue > 1000


The script also computes total company revenue across all products.

🛠️ Technologies Used

Python 3

Pandas

OS module

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/sales-data-analysis.git


Navigate to the project folder:

cd sales-data-analysis


Install dependencies:

pip install pandas


Run the script:

python analysis.py

📈 Sample Output
==============================
   DATA ANALYSIS REPORT
==============================

[Raw Data with Revenue Calculation]:
   Product  Price  Units_Sold  Total_Revenue
0   Laptop   1000           5           5000
1    Mouse     25          50           1250
2  Monitor    300          10           3000
3 Keyboard     80          20           1600
4   Webcam    120          15           1800

[High Value Transactions]:
   Product  Price  Units_Sold  Total_Revenue
0   Laptop   1000           5           5000
1    Mouse     25          50           1250
2  Monitor    300          10           3000
3 Keyboard     80          20           1600
4   Webcam    120          15           1800

------------------------------
TOTAL COMPANY REVENUE: $12650
------------------------------

🎯 Use Cases

Beginner Python & Pandas practice

Simple ETL / data transformation demo

Data Analyst portfolio project

Interview explanation of data processing logic

🔮 Possible Enhancements

Export results to a new CSV or Excel file

Add visualizations using Matplotlib / Seaborn

Accept dynamic thresholds for high-value sales

Integrate with a database (PostgreSQL / SQLite)

Convert into a reusable CLI tool

👤 Author

Rahul Deevanapalli
Data Science | Data Analytics | Machine Learning
