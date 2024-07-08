from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    text = browser.find_element(By.ID, "input_value").text
    answer = calc(text)

    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()