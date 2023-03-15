import requests
from bs4 import BeautifulSoup
import time
import json

def log_yello():
  
    response = requests.get('http://192.168.178.21/')
    soup = BeautifulSoup(response.text, 'html.parser')
    number = soup.find(class_='whats').text.strip()

    log_data = {'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"), 'value': number}

    with open('log.json', 'a') as f:
        json.dump(log_data, f)
        f.write('\n')

while True:
    log_yello()
    time.sleep(300) # 5 minutes