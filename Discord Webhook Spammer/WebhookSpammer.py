import json
import requests
import time
from colorama import Fore, Style

# Load configuration from config.json file
with open('config.json') as f:
    config = json.load(f)

# Extract message and webhook from config
message = config['Message']
webhook_url = config['Webhook']

# Continuously send the message until program is closed
while True:
    # Send message to webhook
    response = requests.post(webhook_url, json={'content': message})
    
    # Check if request was successful
    if response.status_code == 204:
        print(f"{Fore.GREEN}[Sent] {Style.RESET_ALL}{message}")
    else:
        print(f"{Fore.RED}[Error] {Style.RESET_ALL}Failed to send message. Status code: {response.status_code}")

