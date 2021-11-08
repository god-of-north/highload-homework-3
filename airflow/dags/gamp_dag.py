from datetime import datetime

from urllib.parse import urlencode
import requests 

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def get_currency_rate(currency):
    r = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    r.raise_for_status()
    for x in r.json():
        if x['cc'] == currency:
            return x['rate']

def send_currency_rate_to_ga(currency, rate):
    params = {
        'v': 1,
        't': 'event',
        'tid': 'UA-211919994-1',
        'cid': '444',
        'dl': 'http://kievblues.pythonanywhere.com/rate',
        'ec': currency,
        'ea': 'rate',
        'ev': int(rate*1000)
    }
    
    url = 'https://www.google-analytics.com/collect?'+urlencode(params)
    r = requests.post(url = url, headers={'User-Agent': 'My User Agent 1.0'}) 
    r.raise_for_status()
    

def send_data():
    print('Requesting currency rate')
    rate = get_currency_rate('USD')
    print('Sending data to GA')
    send_currency_rate_to_ga('USD', rate)
    print('Done')

default_args = {
    'owner': 'lesyk_maksym',
    'email': ['kiev.blues@gmail.com'],
    'email_on_failure': False,
    'retries': 2
}

with DAG(
    'gamp_dag',
    description='Send currency rate to Google Analytics via Measurement Protocol',
    schedule_interval='@daily',
    start_date=datetime(2021,11,5,9,0),
    default_args=default_args
) as dag:

    send_data_task = PythonOperator(
        task_id='send_to_ga',
        dag=dag,
        python_callable=send_data,
    )
