import requests
import os
import time
import random
import datetime


while True:
    error_file = open("error.log", "a")
    success_file = open("access.log", "a")
    time.sleep(random.randint(30, 60))
    try:
        URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        response = requests.get(URL)
        PB = response.json()
        print(PB)
        today = datetime.datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
        success_file.write("| "+os.getlogin()+" | "+today +
                           " | "+str(response.status_code)+" "+str(response.reason)+" Operation success!"+"\n")
    except Exception as e:
        today = datetime.datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
        error_file.write("| "+os.getlogin()+" | "+today +
                         " | "+str(response.status_code)+" "+str(response.reason)+" "+str(e)+"\n")
    except Exception:
        success_file.close()
        error_file.close()
