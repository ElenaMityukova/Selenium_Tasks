from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


def submit():
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value")
    res = calc(x.text)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(res)
    submit()

finally:
    sleep(30)
    browser.quit()
