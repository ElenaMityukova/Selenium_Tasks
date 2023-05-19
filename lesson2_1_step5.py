from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(y)

    option_checkbox = browser.find_element(By.ID, "robotCheckbox")
    option_checkbox.click()
    option_radiobutton = browser.find_element(By.ID, "robotsRule")
    option_radiobutton.click()

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    sleep(30)
    browser.quit()
