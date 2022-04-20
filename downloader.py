import os
import time
# importing webdriver from selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from os import listdir
from os.path import isfile, join

print("open file with links")
links = open('file.txt').readlines()

print("set path to Cromium.exe here")
driver = webdriver.Chrome(executable_path=r'XXX\chromedriver.exe')
url = "https://link.springer.com"
driver.get(url)
driver.find_element(By.XPATH, "//*[@id='home-page']/section/div/div[2]/button[1]").click() #cookies
driver.find_element(By.XPATH, "//*[@id='header']/div[1]/div[1]/a").click() # login
driver.find_element(By.XPATH, "//*[@id='athens-shibboleth-link']").click() #institution


actions = ActionChains(driver)
print("Select UNI by entering name")
actions.send_keys('TUM')
actions.send_keys(Keys.ENTER)
actions.perform()
actions.reset_actions()
time.sleep(0.5)

driver.find_element(By.XPATH, "//*[@id='content']/div[2]/ul/li[3]/a").click() #Selecting tum


actions = ActionChains(driver)
print("enter Username")
actions.send_keys('Username')
actions.send_keys(Keys.TAB)
print("enter Password")
actions.send_keys('Password')
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()


print("Set chromium to download of pdf insted of open")


input("Press Enter to continue...")

for link in links:

    onlyfiles = [f for f in listdir("C:/Users/naliv/Downloads") if isfile(join("C:/Users/naliv/Downloads", f))]
    string = ' '.join(onlyfiles)

    while "crdownload" in string:
        time.sleep(1)
        onlyfiles = [f for f in listdir("C:/Users/naliv/Downloads") if isfile(join("C:/Users/naliv/Downloads", f))]
        string = ' '.join(onlyfiles)

    link = link.replace("\n", "")
    link = link.split("/")

    link = "https://link.springer.com/content/pdf/" + link[-2] + "%2F" + link[-1] + ".pdf"

    driver.get(link)
    time.sleep(5)





