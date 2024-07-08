from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    answer = calc(browser.find_element(By.ID,"input_value").text)
    browser.find_element(By.ID,"answer").send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла