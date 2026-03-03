# Project: Automating filling in products in a system using pyautogui
#
# This this code does:
# 1. Open Brave Browser
# 2. Log in to the system
# 3. Read database
# 4. Write in products repeately
#
# IMPORTANT INFO FOR READERS
# this code is just a simple exercise of how to automate tasks
# using pyautogui and pandas. This is not a real project and 
# works only for my machine. If it works on yours, thats a hell of a coincidence.
# Also, the table is in portuguese, so dont mind the texts.

# package imports
import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 1

table = pd.read_csv('produtos.csv')
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# 1. Open Brave Browser
pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

# 2. Log in to the system
pyautogui.click(x=1016, y=480) # click in the email field
pyautogui.write('email@gmail.com')
pyautogui.press('tab') # move to the password field
pyautogui.write('12345678')
pyautogui.press('enter') # log in
time.sleep(3)

# 3. Read database (already done in the beginning of the code)
# 4. Write in products repeately

for i in table.index:

    pyautogui.click(x=1000, y=375) # click in the first field
    #fill in the fields:
    pyautogui.write(str(table.loc[i, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[i, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[i, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[i, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[i, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[i, 'custo']))
    pyautogui.press('tab')
    obs = table.loc[i, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
    #scroll up to the top