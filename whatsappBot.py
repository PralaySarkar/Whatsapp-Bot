#!/usr/bin/env python
__author__ = "Pralay Sarkar || CSE || Indian Institute of Information Technology Kalyani"
__copyright__ = "Copy Right @ 2020"
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('./chromedriver') #path to latest chromedriver binary

driver.get("https://web.whatsapp.com/") #open for this URL
wait = WebDriverWait(driver, 60)

target = '"Go Corona Go"' #contact name of target. could be individual or group chat

string = "You messed with the wrong hacker. You all are HACKED!" #type your message what you want to send

x_arg = '//span[contains(@title,' + target + ')]'
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) #locate the target chat element
group_title.click() #click on the target chat element
inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
input_box = wait.until(EC.presence_of_element_located(( By.XPATH, inp_xpath))) #locate the input box element
i = 0 #counter variable to count number of messages
while(True): #iterate infinitely
	input_box.send_keys(string + Keys.ENTER) #enter message in input box and press enter
	time.sleep(1) #send messages every 1 second
	i += 1
	sys.stdout.write("\rMessages sent:  %i" % i)
	sys.stdout.flush()
