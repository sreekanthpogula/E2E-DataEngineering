from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    # Define tasks
    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    # Set task dependencies
    start >> end