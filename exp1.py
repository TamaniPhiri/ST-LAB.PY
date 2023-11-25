from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Initialize the webdriver using GeckoDriver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

url = "https://www.google.com/"
driver.get(url)
