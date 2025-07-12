import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch

# DB connection info
DB_CONFIG = {
    'host': 'ep-bold-glitter-ae36genb-pooler.c-2.us-east-2.aws.neon.tech',
    'port': 5432,
    'database': 'neondb',
    'user': 'neondb_owner',
    'password': 'npg_OhjX4zcs8xdI',
    'sslmode': 'require',
}

def connect_db():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def load_customers(csv_path):
    print(f"Loading customers from: {csv_path}")
    df = pd.read_csv(csv_path)
    conn = connect_db()
    cur = conn.cursor()

    insert_query = """
    INSERT INTO customers (customer_id, first_name, last_name, email, created_at)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (customer_id) DO NOTHING;
    """

    data = df[['customer_id', 'first_name', 'last_name', 'email', 'created_at']].values.tolist()
    execute_batch(cur, insert_query, data)
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {len(data)} customers.")

def load_orders(csv_path):
    print(f"Loading orders from: {csv_path}")
    df = pd.read_csv(csv_path)
    conn = connect_db()
    cur = conn.cursor()

    insert_query = """
    INSERT INTO orders (order_id, customer_id, order_date, total_amount, status)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (order_id) DO NOTHING;
    """

    data = df[['order_id', 'customer_id', 'order_date', 'total_amount', 'status']].values.tolist()
    execute_batch(cur, insert_query, data)
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {len(data)} orders.")

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    load_customers(os.path.join(current_dir, 'data/customers.csv'))
    load_orders(os.path.join(current_dir, 'data/orders.csv'))
