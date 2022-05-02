from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

action = ActionChains(driver)

driver.get("https://www.instagram.com")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys('prefacelikebot')
driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys('Qpalzm971208')
driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys('prefacecoding')
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()

time.sleep(10)

#get the number of posts
number_of_posts = int(driver.find_element(By.CLASS_NAME, 'g47SY').text.replace(',',''))
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()

time.sleep(5)
for loop in range(1, number_of_posts+1):
    if loop == 1:
        action = ActionChains(driver)
        # aciton.double_click(driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/button"))
        driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
        time.sleep(2)
    else:
        driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
        time.sleep(2)

print("done")