# import mechanize
#
# browser = mechanize.Browser()
# # browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; es-VE;  rv:1.9.0.1)Gecko/2008071615 Debian/6.0 Firefox/9')]
# browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.61')]
# browser.set_handle_robots(False)
# browser.open('http://facebook.com/pokes')

# fill in facebook login information, or pass in through environment variables
LOGIN_EMAIL = ''
LOGIN_PASS = ''

import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://facebook.com/pokes')

if 'https://www.facebook.com/login.php' in driver.current_url:
    email = driver.find_element_by_xpath("//input[@id='email']")
    password = driver.find_element_by_xpath("//input[@id='pass']")
    email.send_keys(LOGIN_EMAIL)
    password.send_keys(LOGIN_PASS)
    driver.find_element_by_id('loginbutton').click()

while True:
    driver.get('http://facebook.com/pokes')
    try:
        button = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Poke Back'))
            )
        button.click()
    except:
        time.sleep(5)
