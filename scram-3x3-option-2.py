from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# If we do end up using this the path will obviously need to be changed, as I do not plan to run a bot off my computer
driver = webdriver.Chrome('./chromedriver')

url = "https://cstimer.net/"

driver.maximize_window()

driver.get(url)

driver.find_element_by_xpath("//span[contains(text(),'next')]").click()

time.sleep(1)

scramble = driver.find_element_by_id('scrambleTxt').text

print(scramble)

driver.close()
