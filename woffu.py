#!/home/alex/.virtualenvs/woffu/bin/python3

# -------------------------------------------------------------------
# Set a cronjob 5 minutes before you clock-in/out
# running this script and forget about using Woffu :)
# -------------------------------------------------------------------

import os
import time
import random
import argparse

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


parser = argparse.ArgumentParser()
parser.add_argument('--action', type=str, required=True, dest='action', choices=['entrada', 'salida'])

args = parser.parse_args()
action = args.action

# --------------------------------------------
URL = 'https://COMPANY-NAME.woffu.com/#/login'
EMAIL = ''
PASSWORD = ''  # Get password from env | os.environ('WOFFU_PASS')
# --------------------------------------------

# To avoid clock-in/out always at the same exact time
random_mins = random.randint(3, 6) * 60
time.sleep(random_mins)

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
wait = WebDriverWait(driver, 10)

driver.get(URL)

# Log in
email = driver.find_element_by_id("tuEmail")
password = driver.find_element_by_id("tuPassword")

email.send_keys(EMAIL)
password.send_keys(PASSWORD)

driver.find_element_by_xpath('//*[@id="intro"]/div/form/span/button').click()

# Wait until the page is loaded
wait.until(lambda driver: driver.find_element_by_class_name('progress-bar'))

if action == 'entrada':
	driver.find_element_by_id("in").click()

elif action == 'salida':
	driver.find_element_by_id("out").click()

driver.quit()
