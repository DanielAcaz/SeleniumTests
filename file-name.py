import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class ChromeSearch(unittest.TestCase):
	
	def setUp(self):
		chrome_options = webdriver.ChromeOptions()
		self.driver = webdriver.Chrome(r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", options=chrome_options)
		self.driver.maximize_window()
	 
	# As per unittest module, individual test should start with test_
	
	def test_search_lambdatest_chrome(self):
		driver_chrome = self.driver
		driver_chrome.get('http://www.google.com')
		time.sleep(10)
		search_criteria = driver_chrome.find_element_by_class_name("gLFyf.gsfi")
		search_criteria.clear()
		search_criteria.send_keys("Lambda Test")
		# Check if the search returns any result
		assert "No results found." not in driver_chrome.page_source
		search_criteria.submit()
		time.sleep(10)
	
	def tearDown(self):
		# Close the browser. 
		self.driver.close()

class FirefoxSearch(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
	 
	# As per unittest module, individual test should start with test_
	def test_search_lambdatest_firefox(self):
		driver_firefox = self.driver
		driver_firefox.get('http://www.google.com')
		time.sleep(10)
		search_criteria = driver_firefox.find_element_by_class_name("gLFyf.gsfi")
		search_criteria.clear()
		search_criteria.send_keys("Lambda Test")
		# Check if the search returns any result
		assert "No results found." not in driver_firefox.page_source
		search_criteria.submit()
		time.sleep(10)

	# Anything declared in tearDown will be executed for all test cases
	def tearDown(self):
	# Close the browser. 
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
