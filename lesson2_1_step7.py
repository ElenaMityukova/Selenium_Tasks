from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number_in_box = browser.find_element(By.ID, "treasure")
    get_number = number_in_box.get_attribute("valuex")
    x = calc(get_number)

    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(x)

    option_checkbox = browser.find_element(By.ID, "robotCheckbox")
    option_checkbox.click()
    option_radiobutton = browser.find_element(By.ID, "robotsRule")
    option_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    sleep(10)
    browser.quit()
