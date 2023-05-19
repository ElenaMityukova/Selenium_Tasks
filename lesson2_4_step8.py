from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button_book = browser.find_element(By.ID, 'book')
    price100 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button_book.click()

    x = browser.find_element(By.ID, "input_value")
    res = calc(x.text)
    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(res)

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()

finally:
    sleep(5)
    browser.quit()
