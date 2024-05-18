# подключаем webdriver - набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера, увидим новое открытое окно браузера
browser = webdriver.Chrome()

# открываем сайт по указанной ссылке
browser.get("http://suninjuly.github.io/simple_form_find_task.html")

# ищем нужный элемент на сайте по его id
button = browser.find_element(By.ID, "submit_button")

# помним, что нужно закрыть окно браузера
browser.quit()
