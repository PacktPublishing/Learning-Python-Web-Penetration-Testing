import requests
from threading import Thread
import sys
import time
import getopt
import re
import md5
from termcolor import colored

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = "http://www.bing.com"
urly = "www.bing.com"
driver = webdriver.PhantomJS()
time.sleep(1)
driver.get(url)
driver.save_screenshot(urly +".png")
driver.quit()
