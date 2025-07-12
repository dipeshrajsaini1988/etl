-- Create customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    total_amount NUMERIC(10, 2),
    status VARCHAR(20)
);

-- Insert sample data into customers
INSERT INTO customers (first_name, last_name, email) VALUES
('Alice', 'Johnson', 'alice@example.com'),
('Bob', 'Smith', 'bob@example.com')
ON CONFLICT DO NOTHING;

-- Insert sample data into orders
INSERT INTO orders (customer_id, order_date, total_amount, status) VALUES
(1, '2025-07-01', 150.75, 'completed'),
(2, '2025-07-02', 299.99, 'pending')
ON CONFLICT DO NOTHING;





