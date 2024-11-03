import requests
import time

server_ip = '192.168.x.x'  

while True:
    try:
        response = requests.get(f'http://192.168.1.9:5000/view_logs')
        if response.status_code == 200:
            logs = response.json().get('logs', [])
            print("Logs received from server:")
            for log in logs:
                print(log)
        else:
            print("Failed to retrieve logs, server responded with:", response.status_code)
    except requests.exceptions.ConnectionError:
        print("Error connecting to server: Connection refused or unreachable.")
    time.sleep(5)
