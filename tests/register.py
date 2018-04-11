from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options)

for i in xrange(200):
    print "Creating TestUser"+str(i)
    driver.get("http://127.0.0.1:8000/Tweety/default/user/register?_next=%2FTweety%2Fdefault%2Fhome")

    first_name = driver.find_element_by_id("auth_user_first_name")
    last_name = driver.find_element_by_id("auth_user_last_name")
    email = driver.find_element_by_id("auth_user_email")
    password = driver.find_element_by_id("auth_user_password")
    password_two = driver.find_element_by_id("auth_user_password_two")
    handle = driver.find_element_by_id("auth_user_handle")

    foo = str(i)
    first_name.send_keys("TestUser" + foo)
    last_name.send_keys("TestUser" + foo)
    email.send_keys("TestUser"+foo+"@gmail.com")
    password.send_keys("asdf")
    password_two.send_keys("asdf")
    handle.send_keys("TestUser" + foo)

    form = driver.find_element_by_css_selector("input[type='submit']")
    form.click()

    driver.get('http://127.0.0.1:8000/Tweety/default/user/logout')
