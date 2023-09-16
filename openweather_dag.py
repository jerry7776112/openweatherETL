from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from openweather_etl import run_openweather_etl

"""Write your information"""
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 15),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

"""Create DAG"""
dag = DAG(
    'openweather_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

"""Operate your Python code"""
run_etl = PythonOperator(
    task_id='complete_openweather_etl',
    python_callable=run_openweather_etl,
    dag=dag, 
)

run_etl