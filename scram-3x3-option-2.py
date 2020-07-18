from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Whatever the script is running on must have Google Chrome installed and webdriver must have permission to run
driver = webdriver.Chrome('./chromedriver')

url = "https://cstimer.net/"

driver.maximize_window()

driver.get(url)

driver.find_element_by_xpath("//span[contains(text(),'next')]").click()

time.sleep(1)

scramble = driver.find_element_by_id('scrambleTxt')

print(scramble)

driver.close()
