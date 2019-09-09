# -------------------------------------------------------------------
# Set a cronjob 5 minutes before you clock-in/out
# running this script and forget about using Woffu :)
# -------------------------------------------------------------------

import os
import time
import random
import argparse
import logging
from logging.handlers import TimedRotatingFileHandler

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


logging_handler = TimedRotatingFileHandler(filename='woffu.log', when='D', interval=30)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO, handlers=[logging_handler])


parser = argparse.ArgumentParser()
parser.add_argument('--action', type=str, required=True, dest='action', choices=['entrada', 'salida'])

args = parser.parse_args()
action = args.action

# --------------------------------------------
URL = f'https://{os.environ('WOFFU_COMPANY')}.woffu.com/#/login'
EMAIL = os.environ('WOFFU_EMAIL')
PASSWORD = os.environ('WOFFU_PASS')
# --------------------------------------------

# To avoid clock-in/out always at the same exact time
random_mins = random.randint(3, 6) * 60
time.sleep(random_mins)

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=chrome_options)
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
	logging.info('Entrada')

elif action == 'salida':
	driver.find_element_by_id("out").click()
	logging.info('Salida')

driver.quit()
