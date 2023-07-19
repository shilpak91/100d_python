from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# To keep browser open
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

chrome_driver_path = "/Users/shilpak/Development/chromedriver"
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.nl/-/en/WH-1000XM5-Cancelling-Wireless-Headphones-Built/dp/B09Y2MYL5C/ref=sr_1_5?crid=3J3882WC9AM6V&keywords=sony%2Bwh-1000xm5&qid=1689793282&sprefix=%2Caps%2C63&sr=8-5&th=1")
cookies = driver.get_cookies()
# print(cookies)
for i in cookies:
    name = i["name"]
    value = i["value"]
    driver.add_cookie({"name" : name , "value" : value})

price = driver.find_elements(By.XPATH,value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[1]')
print(price)



driver.quit()