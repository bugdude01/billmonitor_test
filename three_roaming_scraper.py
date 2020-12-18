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
		#look for an instance of a "flag-link", these only appear on the two-column table pages.
		nation = driver.find_element_by_xpath("//*[@class='flag-links']/img[@alt]")
		print("Mobile roaming in " + nation.get_attribute("alt") + " - Support - Three")

		# if found then look for the data within the table for both monthly and PAYG
		paym_cost_1 = driver.find_element_by_xpath("//*[@class='roaming-charges-table']/tbody/tr[1]/td").text
		paym_cost_2 = driver.find_element_by_xpath("//*[@class='roaming-charges-table']/tbody/tr[3]/td").text
		paym_cost_3 = driver.find_element_by_xpath("//*[@class='roaming-charges-table']/tbody/tr[5]/td").text
		paym_cost_4 = driver.find_element_by_xpath("//*[@class='roaming-charges-table']/tbody/tr[7]/td").text
		print("Pay monthly")
		print("Calling a UK number - " + paym_cost_1)
		print("Texts to UK - " + paym_cost_2)
		print("Receiving calls from any number - " + paym_cost_3)
		print("Using internet and data - " + paym_cost_4)

		print(" ")

		# click to PAYG table and find PAYG costs
		paygLink = driver.find_element_by_link_text("Pay As You Go")
		paygLink.click()

		payg_cost_1 = driver.find_element_by_xpath("//*[@id='panel2']/section[2]/table/tbody/tr[1]/td").text
		payg_cost_2 = driver.find_element_by_xpath("//*[@id='panel2']/section[2]/table/tbody/tr[3]/td").text
		payg_cost_3 = driver.find_element_by_xpath("//*[@id='panel2']/section[2]/table/tbody/tr[5]/td").text
		payg_cost_4 = driver.find_element_by_xpath("//*[@id='panel2']/section[2]/table/tbody/tr[7]/td").text
		print("PAYG")
		print("Calling a UK number - " + payg_cost_1)
		print("Texts to UK - " + payg_cost_2)
		print("Receiving calls from any number - " + payg_cost_3)
		print("Using internet and data - " + payg_cost_4)

		print(" ")
		print("Next Country ")
		print(" ")

	except:
		# otherwise look for the relevant data within the three-column table for both monthly and PAYG

		print(driver.title)
		# find pay monthly costs
		paym_cost_1 = driver.find_element_by_xpath("//*[@class='clearfix']/tbody/tr[1]/td[2]").text
		paym_cost_2 = driver.find_element_by_xpath("//*[@class='clearfix']/tbody/tr[3]/td[2]").text
		paym_cost_3 = driver.find_element_by_xpath("//*[@class='clearfix']/tbody/tr[5]/td[2]").text
		paym_cost_4 = driver.find_element_by_xpath("//*[@class='clearfix']/tbody/tr[7]/td[2]").text
		print("Pay monthly")
		print("Calling a UK number - " + paym_cost_1)
		print("Texts to UK - " + paym_cost_2)
		print("Receiving calls from any number - " + paym_cost_3)
		print("Using internet and data - " + paym_cost_4)
		print(" ")

		# click to PAYG table and find PAYG costs
		paygLink = driver.find_element_by_link_text("Pay As You Go")
		paygLink.click()

		payg_cost_1 = driver.find_element_by_xpath("//*[@class='clearfix']/tbody/tr[1]/td[2]").text
		payg_cost_2 = driver.find_element_by_xpath("//*[@class='clearfix']/tbody/tr[3]/td[2]").text
		payg_cost_3 = driver.find_element_by_xpath("//*[@class='clearfix']/tbody/tr[5]/td[2]").text
		payg_cost_4 = driver.find_element_by_xpath("//*[@class='clearfix']/tbody/tr[7]/td[2]").text
		print("PAYG")
		print("Calling a UK number - " + payg_cost_1)
		print("Texts to UK - " + payg_cost_2)
		print("Receiving calls from any number - " + payg_cost_3)
		print("Using internet and data - " + payg_cost_4)

		print(" ")
		print("Next Country ")
		print(" ")


	# go back to roaming abroad home page via initial link as bredcrumbs not consistent on older pages
	driver.get("http://www.three.co.uk/Support/Roaming_and_international/Roaming_abroad")

driver.quit()
