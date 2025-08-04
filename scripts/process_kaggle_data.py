import pandas as pd
import os

# Load the downloaded data
data_path = r"C:\Users\heman\.cache\kagglehub\datasets\fahmidachowdhury\e-commerce-sales-analysis\versions\1"
df = pd.read_csv(os.path.join(data_path, "ecommerce_sales_analysis.csv"))

print("Original data shape:", df.shape)
print("\nData overview:")
print(df.info())

# Create normalized tables
# 1. Products table
products = df[['product_id', 'product_name', 'category', 'price']].copy()
print(f"\nProducts table: {products.shape}")

# 2. Reviews table  
reviews = df[['product_id', 'review_score', 'review_count']].copy()
print(f"Reviews table: {reviews.shape}")

# 3. Sales table (normalize monthly sales)
sales_data = []
for month in range(1, 13):
    month_col = f'sales_month_{month}'
    for _, row in df.iterrows():
        sales_data.append({
            'product_id': row['product_id'],
            'month': month,
            'sales_amount': row[month_col]
        })

sales = pd.DataFrame(sales_data)
print(f"Sales table: {sales.shape}")

# Show sample data
print("\n=== PRODUCTS SAMPLE ===")
print(products.head())
print("\n=== REVIEWS SAMPLE ===")  
print(reviews.head())
print("\n=== SALES SAMPLE ===")
print(sales.head(10))

# Save processed data
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)

products.to_csv(f"{output_dir}/products.csv", index=False)
reviews.to_csv(f"{output_dir}/reviews.csv", index=False)
sales.to_csv(f"{output_dir}/sales.csv", index=False)

print(f"\nProcessed data saved to {output_dir}/")