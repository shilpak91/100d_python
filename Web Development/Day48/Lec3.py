from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# To keep browser open
# chrome_options = Options()
# chrome_options.add_experimental_option('detach', True)

chrome_driver_path = "/Users/shilpak/Development/chromedriver"
driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_elements(By.ID,value="articlecount")
print(articles[0].text)

articles_num = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
print(articles_num.text)


driver.quit()