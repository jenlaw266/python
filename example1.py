from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)

search = driver.find_element(By.NAME, "q")
search.send_keys("征服异界从游戏开始")
search.send_keys(Keys.RETURN)

# main = driver.find_element_by_class_name("main")

# print(driver.page_source)

# driver.navigate("file:///race_condition.html")
main = WebDriverWait(driver, timeout=3).until(
    lambda d: d.find_element(By.CLASS_NAME, "main"))

articles = main.find_elements(By.CLASS_NAME, "g")
for article in articles:
    header = article.find_element(By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md")
    print(header.text)

time.sleep(5)

driver.close()
# driver.quit()
