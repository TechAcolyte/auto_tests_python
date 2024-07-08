from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x,y):
  return str(int(x) + int(y))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.ID,"num1").text
    second = browser.find_element(By.ID,"num2").text

    asnwer = calc(first, second)
    select = Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(asnwer)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()