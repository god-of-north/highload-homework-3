from urllib.parse import urlencode
import requests 

params = {
    'v': 1,
    't': 'pageview',
    'tid': 'UA-211919994-1',
    'cid': '555',
    'dh': 'kievblues.pythonanywhere.com',
    'dp': '/gmap_test',
    'dt': 'tes-test-test'
}

url = 'https://www.google-analytics.com/collect?'+urlencode(params)

r = requests.post(url = url, headers={'User-Agent': 'My User Agent 1.0'}) 
print(r)
