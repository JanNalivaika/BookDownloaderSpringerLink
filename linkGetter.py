import os
import time
# importing webdriver from selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

print("set folder path here")
os.chdir(r'XXXXX')
print("set path to downloads here")
path_to_downloads = r'XXX'
# Here Chrome  will be used
print("set path to Cromium.exe here")
driver = webdriver.Chrome(executable_path=r'XXX\chromedriver.exe')

# URL of website
url = "https://link.springer.com"

# Opening the website
driver.get(url)
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='home-page']/section/div/div[2]/button[1]").click() #cookies
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='header']/div[1]/div[1]/a").click() # login
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='athens-shibboleth-link']").click() #institution
time.sleep(0.5)

actions = ActionChains(driver)
print("Select UNI by entering name")
actions.send_keys('TUM')
actions.send_keys(Keys.ENTER)
actions.perform()
actions.reset_actions()
time.sleep(0.5)

driver.find_element(By.XPATH, "//*[@id='content']/div[2]/ul/li[3]/a").click() #Selecting tum
time.sleep(0.5)

actions = ActionChains(driver)
print("enter Username")
actions.send_keys('Username')
actions.send_keys(Keys.TAB)
print("enter Password")
actions.send_keys('Password')
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
time.sleep(0.5)
actions.perform()


driver.find_element(By.XPATH, "//*[@id='Discipline']/ol/li[8]/a").click() #selecting enginerring
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='content-type-facet']/ol/li[4]/a/span[2]").click() #Selecting book
time.sleep(0.5)

input("Open book category and Press Enter to continue...")


driver.find_element(By.XPATH, "//*[@id='results-only-access-checkbox']").click() #exclude blocked content
time.sleep(0.5)



slides = driver.find_element(By.XPATH, "//*[@id='kb-nav--main']/div[2]/form/span[2]/span[2]").get_attribute("innerHTML")

for _ in range(int(slides.replace(",",""))):
    Links = []
    Buttons = driver.find_elements(By.XPATH, '//a[@class="title"]')
    for button in Buttons:

        text = button.get_attribute("href")
        print("Saving links as a .txt file")
        f = open("file.txt", "a")
        f.write(text)
        f.write("\n")
        f.close()

    driver.find_element(By.CLASS_NAME, "next").click() #exclude blocked content
    time.sleep(0.5)


