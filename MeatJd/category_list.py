
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium import webdriver
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome('/users/wangkaixi/desktop/chromedriver')
driver.get("https://item.jd.com/65330355052.html")

print(driver.page_source)
