
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()

# Open the desired webpage
driver.get('https://www.saucedemo.com/')

# Locate the username field, password field and login button
username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')

# Enter the credentials and log in
username.send_keys('standard_user')
password.send_keys('secret_sauce')
login_button.click()

# Wait for the page to load completely
time.sleep(5)

# 1. Get the title of the webpage
title = driver.title
print("Title of the webpage:", title)

# 2. Get the current URL of the webpage
current_url = driver.current_url
print("Current URL of the webpage:", current_url)

# 3. Extract the entire contents of the webpage
page_source = driver.page_source

# Save the contents to a text file
with open("Webpage_task_11.txt", "w", encoding='utf-8') as file:
    file.write(page_source)

# Close the WebDriver
driver.quit()