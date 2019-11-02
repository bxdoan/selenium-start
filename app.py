import time
import random
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print('Opening Chrome')
# Download chromedriver from https://chromedriver.storage.googleapis.com/index.html?path=2.35/
# Access the webdriver via its full path
browser = webdriver.Chrome(dir_path + '/chromedriver')
print('Accessing Yahoo.com')
browser.get('http://www.yahoo.com')

time.sleep(2)

print('Finding search box')
elem = browser.find_element_by_name('p')  # Find the search box
print('Searching for seleniumhq')
elem.send_keys('seleniumhq' + Keys.RETURN)

# Randomising wait time to mimic humans!
time.sleep(random.randint(0, 5))

print('Quitting browser')
browser.quit()