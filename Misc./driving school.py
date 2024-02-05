import selenium
from selenium import webdriver
import pandas as pd
import time
import pyautogui as py
from time import sleep
from pyperclip import paste


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

'''
TO-DO:
- Change quiz question detection to detect if lock is present
- parse quiz question (true false)
- Get timing right
- Stop at progress assessment
- Do progress assessment?????
'''

#disclaimer
import os
for i in range(5, -1, -1):
    os.system('cls')
    print('SWITCH TO CHATGPT!')
    print(i)
    sleep(1)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path='chromedriver-win64')
browser = webdriver.Chrome()


#helper functions 
def movemouse(path):
    action = webdriver.ActionChains(browser)
    element = browser.find_element('xpath', path) # or your another selector here
    action.move_to_element(element)
    action.perform()


def feedsleep():
    #Get feedback
    time.sleep(3.0)
    browser.find_element('xpath', '/html/body/div[6]/div[1]/a').click()

def submitvalue(path, p):
    browser.find_element('xpath', path).send_keys(p)
    print(p)

#login info
testname = 'or2tx2017@gmail.com'
testpass = 'Thisisasecurepassword!646'

browser.get('https://nationalhighwaysafetyadministration.com/Acp')
browser.implicitly_wait(15)

#log into website
browser.find_element("xpath", "/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[2]/ion-col/ion-card/ion-list/ion-item[1]/div[1]/div/ion-input/input").send_keys(testname)
browser.find_element("xpath", "/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[2]/ion-col/ion-card/ion-list/ion-item[2]/div[1]/div/ion-input/input").send_keys(testpass)
browser.find_element('xpath','/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[2]/ion-col/ion-card/div[2]/button[2]/span').click()


#click on course
browser.find_element('xpath', '//*[@id="accordion-header-0"]/div[1]').click()
browser.find_element('xpath', '//*[@id="accordion-body-0"]/div/ion-row/ion-col[3]/div/button/span/span').click()

#switch to course tab
browser.switch_to.window(browser.window_handles[1])

#wait function (stack overflow: https://stackoverflow.com/questions/26086965/wait-until-loader-disappears-python-selenium)
# for i in range(5):
#     sleep(1)
#     print(i)
try:
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(('xpath', '/html/body/app-root/course/div/div[1]/i')))
except TimeoutException:
    print("error")
sleep(3)
# print(browser.find_element('id', 'mainContent').text)
pron = "this is pron"
browser.implicitly_wait(10)
#iterating through pages
while True:
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(('xpath', '/html/body/app-root/course/div/div[4]/i')))
        browser.find_element(By.XPATH, '/html/body/app-root/course/div/div[4]/i').click()
    except:
        browser.implicitly_wait(2)
        print("quiz question")
        browser.find_element(By.XPATH, '/html/body/app-root/course/div/div[1]/i').click()
        sleep(1.5)
        pron = browser.find_element('id', 'mainContent').text
        print(browser.find_element('id', 'mainContent').text)
    
        browser.find_element(By.XPATH, '/html/body/app-root/course/div/div[4]/i').click()
        sleep(1.5)
        pron += browser.find_element('id', 'mainContent').text
        with py.hold('alt'):
            py.press('tab')
            sleep(.1)
        sleep(.5)
        py.leftClick(750, 950)
        sleep(.5)
        py.write(pron.replace('\n', ' ') + " answer the question by replying with only the letters a b or c. if the question is true or false, reply with only the letters a or b", 0.004)
        sleep(.5)
        py.leftClick(1575, 943)
        sleep(3.5)
        py.leftClick(740, 840)
        sleep(1)
        print(paste())
        with py.hold('alt'):
            py.press('tab')
        browser.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/test/div/div/form/div[1]/div/div/div[' + chr(ord(paste()[0]) - 48) +']').click()
        browser.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/test/div/div/form/div[3]/div/button').click()
        browser.find_element(By.XPATH, '/html/body/app-root/course/div/div[4]/i').click()
#position
# import pyautogui as py
# while True:
#     print(py.position(), end = "\r")

#window switching test [FAIL]

#chatgpt
# import openai
# openai.api_key = "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"
# respone = openai.completions.create(model="gpt-3.5-turbo", prompt=pron)
# print(respone)

#hold screen
input()