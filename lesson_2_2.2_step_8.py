import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'firstname')
    last_name = browser.find_element(By.NAME, 'lastname')
    email = browser.find_element(By.NAME, 'email')
    forms = [first_name, last_name, email]
    for element in forms:
        element.send_keys("print_smth_here")

    file = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'ElenaD.txt')
    file.send_keys(file_path)
    #file.send_keys("C:/Users/helen/PycharmProjects/Selenium_course/lesson_2/ElenaD.txt")

    print(os.path.abspath(os.path.dirname(__file__)))
    print(os.path.abspath(__file__))
    print(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    sleep(30)
    browser.quit()
