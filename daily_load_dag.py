from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import sys

# Add your ETL folder to sys.path if needed
etl_path = os.path.join(os.path.dirname(__file__), 'etl')
if etl_path not in sys.path:
    sys.path.append(etl_path)

from load_csv_to_neon import load_customers, load_orders

default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 13),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'daily_load_csv_to_neon',
    default_args=default_args,
    schedule_interval='0 2 * * *',  # every day at 2 AM
    catchup=False
)

def run_load():
    from datetime import datetime
    today_str = datetime.today().strftime('%Y%m%d')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    customers_file = os.path.join(base_dir, 'etl', f'customers_{today_str}.csv')
    orders_file = os.path.join(base_dir, 'etl', f'orders_{today_str}.csv')

    load_customers(customers_file)
    load_orders(orders_file)

load_task = PythonOperator(
    task_id='load_csv_files',
    python_callable=run_load,
    dag=dag
)
