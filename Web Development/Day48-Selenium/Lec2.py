from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# To keep browser open
# chrome_options = Options()
# chrome_options.add_experimental_option('detach', True)

chrome_driver_path = "/Users/shilpak/Development/chromedriver"
driver = webdriver.Chrome()


driver.get("https://www.python.org")

event_time = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")

event_name = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")

# event_dict = {n: {"time" : event_time[n].text , "name": event_name[n].text} for n in range(len(event_time))}
print(event_dict)
events = {}

for n in range(len(event_time)):
    events[n] = {"time" : event_time[n].text , "name": event_name[n].text}

print(events)

# for time in event_time:
#     print(time.text)

# for name in event_name:
#     print(name.text)