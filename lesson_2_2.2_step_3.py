from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    total = int(num1.text) + int(num2.text)

    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_visible_text(str(total))

    #browser.find_element(By.TAG_NAME, "select").click()
    #browser.find_element(By.CSS_SELECTOR, f"[value='{total}']").click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    sleep(5)
    print(total)
    browser.quit()
