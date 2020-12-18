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

countries = ["Brazil", "South Africa", "Portugal", "Chile", "Iceland", "China", "Madagascar"]

# Loop through countries
for country in countries:

	search = driver.find_element_by_id("input-append-demo")
	search.clear()
	search.send_keys(country)
	search.send_keys(Keys.RETURN)

	try: 
		nation = driver.find_element_by_xpath("//*[@class='flag-links']/img[@alt]")
		print("Mobile roaming in " + nation.get_attribute("alt") + " - Support - Three")

	except:

		print(driver.title)

	three_col_table = driver.find_element_by_class_name("clearfix")

	# Driver Title should give title of current country page - can pull this off later to head
	# up details of scraped info

	# *** UPDATE *** Different pages present different tables. 2 column tables don't display the
	# country in "driver.title" but DO show country in flag "Alt-text". need to setablish 
	# what table is on the page and then either print driver.title OR flag-links alt-text

	#if two_col_table:


	# go back to roaming abroad home page via initial link as bredcrumbs not consistent on older pages
	driver.get("http://www.three.co.uk/Support/Roaming_and_international/Roaming_abroad")

#driver.quit()
