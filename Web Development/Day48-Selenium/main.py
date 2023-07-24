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

# start_time = datetime.now()
# end_time = start_time + timedelta(seconds=5)

# start_time = start_time.strftime("%H:%M:%S")
# end_time = end_time.strftime("%H:%M:%S")

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [item.get_attribute("id") for item in items]
item_ids = item_ids[:-1]

game_on = True

while game_on:

    cookie.click()

    # game_end_time = datetime.now()
    # game_end_time = game_end_time.strftime("%H:%M:%S")
    if time.time() > timeout:
    #     game_on = False
    # time.sleep(0.005)

        # Get Current cookie count
        current_cookie_count = driver.find_element(By.ID,value="money")
        current_cookie = int(current_cookie_count.text.strip().replace(',',''))

        # Get all available upgrades
        all_avail_upgrades = driver.find_elements(By.CSS_SELECTOR,value="#store b")
        all_avail_upgrades = all_avail_upgrades[:-1]
        # print(all_avail_upgrades)

        # Get price for upgrades
        item_price = []
        for item in all_avail_upgrades:
            all_item = item.text.split("-")[1]
            item_price.append(int(all_item.strip().replace(',','')))

        # print(item_price)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_price)):
            cookie_upgrades[item_price[n]] = item_ids[n]

        # print(cookie_upgrades)


        # Checking max available upgrades
        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if current_cookie > cost:
                affordable_upgrades[cost] = id

        # print(affordable_upgrades)
        highest_price_affordable_upgrade = max(affordable_upgrades)
        # print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        # Get most costly upgrade
        driver.find_elements(By.ID,to_purchase_id)[0].click()

        #Add another 5 seconds until the next check
        timeout = time.time() + 5


    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID,"cps").text
        print(cookie_per_s)
        game_on = False