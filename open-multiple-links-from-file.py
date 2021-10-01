import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

#driver.get("http://onlinenotessharing.epizy.com")

#open file and read lines
file_Stored = input("Input the location of file:")
file_to_login = open(file_Stored, 'r')
Lines = file_to_login.readlines()
driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

#read string before and after : symbol
count=0
for line in Lines:
    count+=1

    #open links for every line
    driver.get(line)

    print("link",count,"opened")
    print("link is",line)

    #open new tab
    driver.execute_script("window.open('');")
    time.sleep(1)
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[count])

    # Switch tab to the new tab, which we will assume is the next one on the right
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    #ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    #driver.find_element_by_css_selector("body").sendKeys(Keys.CONTROL + "t")

time.sleep(2)
driver.quit()
