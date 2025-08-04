-- Real E-commerce Database Schema for Kaggle Dataset
-- Natural Language to SQL Query Generator

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Create reviews table  
CREATE TABLE IF NOT EXISTS reviews (
    product_id INTEGER PRIMARY KEY,
    review_score DECIMAL(3,2) NOT NULL,
    review_count INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create sales table
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    month INTEGER NOT NULL CHECK (month >= 1 AND month <= 12),
    sales_amount INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Load data from CSV files
\copy products FROM '/data/processed/products.csv' WITH CSV HEADER;
\copy reviews FROM '/data/processed/reviews.csv' WITH CSV HEADER;  
\copy sales FROM '/data/processed/sales.csv' WITH CSV HEADER;

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
CREATE INDEX IF NOT EXISTS idx_sales_product_id ON sales(product_id);
CREATE INDEX IF NOT EXISTS idx_sales_month ON sales(month);
CREATE INDEX IF NOT EXISTS idx_reviews_score ON reviews(review_score);

-- Verify data loaded correctly
SELECT 'Products loaded:' as status, COUNT(*) as count FROM products;
SELECT 'Reviews loaded:' as status, COUNT(*) as count FROM reviews;  
SELECT 'Sales records loaded:' as status, COUNT(*) as count FROM sales;