import pandas as pd
import os

# --- STEP 1: PREPARE SAMPLE DATA ---
# This creates a file automatically so the code is "plug and play"
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Webcam'],
    'Price': [1000, 25, 300, 80, 120],
    'Units_Sold': [5, 50, 10, 20, 15]
}
df_raw = pd.DataFrame(data)
df_raw.to_csv('sales_data.csv', index=False)

def run_analysis(filename):
    """Loads a CSV, calculates total revenue, and filters high-value sales."""
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    # Load
    df = pd.read_csv(filename)

    # Transform (Logic)
    df['Total_Revenue'] = df['Price'] * df['Units_Sold']
    
    # Filter: High Value Sales (Revenue > 1000)
    high_value = df[df['Total_Revenue'] > 1000]

    # Summary Stats
    total_business_revenue = df['Total_Revenue'].sum()

    # --- STEP 2: THE OUTPUT ---
    print("="*30)
    print("   DATA ANALYSIS REPORT")
    print("="*30)
    print("\n[Raw Data with Revenue Calculation]:")
    print(df)
    
    print("\n[High Value Transactions]:")
    print(high_value)
    
    print("\n" + "-"*30)
    print(f"TOTAL COMPANY REVENUE: ${total_business_revenue}")
    print("-"*30)

if __name__ == "__main__":
    run_analysis('sales_data.csv') 