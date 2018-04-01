from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import thread
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

def login(driver, foo):
    driver.get("http://127.0.0.1:8000/Tweety/default/user/login?_next=%2FTweety%2Fdefault%2Fhome")
    #print "Logging in TestUser"+foo
    email = driver.find_element_by_id("auth_user_email")
    password = driver.find_element_by_id("auth_user_password")
    email.send_keys("TestUser"+foo+"@gmail.com")
    password.send_keys("asdf")
    form = driver.find_element_by_css_selector("input[type='submit']")
    form.click()
    driver.get_screenshot_as_file('capture.png')
def post(foo, body):
    driver = webdriver.Chrome(chrome_options=chrome_options)
    login(driver, foo)
    driver.get("http://127.0.0.1:8000/Tweety/default/home")
    #print "Posting " + body + " as TestUser"+foo
    text_body = driver.find_element_by_id("cheeps_body")
    text_body.send_keys(body)
    form = driver.find_element_by_css_selector("input[type='submit']")
    form.click()
    driver.get_screenshot_as_file('capture.png')


try:
    for i in xrange(10):
        thread.start_new_thread(post, (str(i), "Tweet #"+str(i)))
except:
    print "Oh no!"

while 1:
    pass
