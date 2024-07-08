from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
button = browser.find_element(By.ID, "book").click()

text = browser.find_element(By.ID, "input_value").text
answer = calc(text)
browser.find_element(By.ID, "answer").send_keys(answer)

browser.find_element(By.ID, "solve").click()

time.sleep(10)