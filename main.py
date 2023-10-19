
import certstream
import requests
import os
from datetime import datetime
import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Config']

def save_website(domain):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_path = 'results'
    file_path = f'{folder_path}/{timestamp}.txt'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path, 'w') as file:
        file.write(domain)

def certstream_callback(message, context):
    if message['message_type'] == "certificate_update":
        all_domains = message['data']['leaf_cert']['all_domains']
        cert_validity = message['data']['leaf_cert']['validity']['end']
        score = message['data']['leaf_cert']['validation']['score']

        if score >= int(config['score_threshold']):
            for domain in all_domains:
                save_website(domain)

config = read_config()

if not os.path.exists('results'):
    os.makedirs('results')

certstream.listen_for_events(certstream_callback)

certstream.run_for(int(config['run_duration_minutes']) * 60)