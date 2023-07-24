from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime,timedelta

# To keep browser open
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

chrome_driver_path = "/Users/shilpak/Development/chromedriver"
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID,value="cookie")

start_time = datetime.now()
end_time = start_time + timedelta(seconds=5)

start_time = start_time.strftime("%H:%M:%S")
end_time = end_time.strftime("%H:%M:%S")

game_on = True

while game_on:
    cookie.click()
    game_end_time = datetime.now()
    game_end_time = game_end_time.strftime("%H:%M:%S")
    if end_time == game_end_time:
        game_on = False
    time.sleep(0.005)

# Get Current cookie count
current_cookie_count = driver.find_element(By.ID,value="money")
current_cookie = int(current_cookie_count.text)

#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [item.get_attribute("id") for item in items]
item_ids = item_ids[:-1]

# Get all available upgrades
all_avail_upgrades = driver.find_elements(By.CSS_SELECTOR,value="#store b")
all_avail_upgrades = all_avail_upgrades[:-1]
# print(all_avail_upgrades)

item_price = []

for item in all_avail_upgrades:
    all_item = item.text.split("-")[1]
    item_price.append(int(all_item.strip().replace(',','')))

# print(item_price)


# Checking max available upgrades
affordable_upgrades = {}
for n in range(len(item_price)):
    if current_cookie > item_price[n]:
        affordable_upgrades[item_ids[n]] = item_price[n]

# print(affordable_upgrades)
max_affordable_value = max(affordable_upgrades.values())


# Get most costly upgrade
get_upgrade = [key for key, val in affordable_upgrades.items() if val == max_affordable_value]
get_upgrade_id = get_upgrade[0]
upgrade = driver.find_elements(By.ID,get_upgrade_id)
upgrade[0].click()


