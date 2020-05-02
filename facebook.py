# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:38:24 2020

@author: Tejas
"""

from selenium import webdriver
import time
import logindata

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('F:\Channel\webdriver\chromedriver.exe', chrome_options=options)
time.sleep(1)

driver.get('http://facebook.com')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="email"]').send_keys(logindata.USERNAME)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(logindata.PASSWORD)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="js_1ai"]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/span').send_keys('This is an automated post from selenium on my facebook news feed.')

driver.find_element_by_xpath('//*[@id="js_2jg"]').send_keys('F:\Channel\Video Thumbnails\Facebook_Automation_Part 1.png')
driver.find_element_by_xpath('//*[@id="js_4tp"]/div[2]/div[3]/div[2]/span/button').click()