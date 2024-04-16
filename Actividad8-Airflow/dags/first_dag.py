from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from datetime import timedelta


def first_function_execute(**context):
    print("First Function Execute")
    context['ti'].xcom_push(key="name", value="Eduardo Gomez")

def second_function_execute(**context):
    instance = context.get("ti").xcom_pull(key="name")
    print(f"Hello {instance} from second function execute")


with DAG(
        dag_id="first_dag",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2024, 4, 14),
        },
        catchup=False) as f:
    first_function_execute = PythonOperator(
        task_id="first_function_execute",
        python_callable=first_function_execute,
        provide_context=True,
        op_kwargs={"my_name":"Ivan Gomez"},)

    second_function_execute = PythonOperator(
        task_id="second_function_execute",
        python_callable=second_function_execute,
        provide_context=True,)

first_function_execute >> second_function_execute