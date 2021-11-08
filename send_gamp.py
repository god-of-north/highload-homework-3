from urllib.parse import urlencode
import requests 

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
    print(r)
    
rate = get_currency_rate('USD')
send_currency_rate_to_ga('USD', rate)
