from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value")
    res = calc(x.text)

    answer_form = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_form)
    answer_form.send_keys(res)

    option_checkbox = browser.find_element(By.ID, "robotCheckbox")
    option_checkbox.click()
    option_radiobutton = browser.find_element(By.ID, "robotsRule")
    option_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    sleep(10)
    browser.quit()
