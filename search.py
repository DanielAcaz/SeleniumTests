# Import the necessary modules for development 
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Invoke a new Firefox Instance 
ff_driver = webdriver.Firefox()
# Blocking wait of 30 seconds in order to locate the element 
ff_driver.implicitly_wait(30)
ff_driver.maximize_window()
# Open the Home Page
ff_driver.get("http://www.google.com")
# Look for the Search Element and enter the Search Criteria 
search_criteria = ff_driver.find_element_by_class_name("gLFyf.gsfi")
search_criteria.clear()
search_criteria.send_keys("Lambda Test")
# Submit the Search results 
search_criteria.submit()
# Sleep for 10 seconds in order to see the results
time.sleep(10)
# Close the Browser instance
ff_driver.close()