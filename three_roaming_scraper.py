from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://www.three.co.uk/Support/Roaming_and_international/Roaming_abroad")
print (driver.title)

search = driver.find_element_by_id("input-append-demo")
search.clear()
search.send_keys("Brazil")
search.send_keys(Keys.RETURN)

# Driver Tite should give title of current country page - can pull this off later to head
# up details of scraped info
print(driver.title)

#driver.quit()
