from math import ceil, pow, pi, e
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/find_link_text"
content = str(ceil(pow(pi, e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.PARTIAL_LINK_TEXT, content)
    button.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Helen")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Drigant")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("SPb")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    print("Все получилось!:)")
finally:
    sleep(10)
    browser.quit()

