from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# To keep browser open
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

chrome_driver_path = "/Users/shilpak/Development/chromedriver"
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com")

fname = driver.find_element(By.NAME , value="fName")
fname.send_keys("Shilpak")

lname = driver.find_element(By.NAME , value="lName")
lname.send_keys("Raich")

email = driver.find_element(By.NAME , value="email")
email.send_keys("sraich@infocepts.com")

submit = driver.find_element(By.CSS_SELECTOR , value="form button")
submit.click()



# driver.quit()