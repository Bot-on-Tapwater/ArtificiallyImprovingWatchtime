'''Generates electronic mail addresses'''

import webbrowser # module that let's us open browser

import random # module that generates random values

import string

from selenium import webdriver # needs to be installed with pip3, allows us to interact with web pages on the browser

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

def openBrowser(): # opens browser and the link provided
    '''
    firefox_path = "/usr/bin/firefox" # path to firefox application

    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path)) # opens firefox application

    webbrowser.get('firefox').open_new_tab('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp') # opens provided link in browser
    '''
    # Specify the path to the Firefox driver executable
    # https://dev.to/eugenedorfling/installing-the-firefox-web-driver-on-linux-for-selenium-d45
    driver_path = '/usr/local/bin/geckodriver' 

    service = Service(executable_path=driver_path )

    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox(service=service) 

    # Navigate to the web page that contains the text field
    driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # element = wait.until(EC.presence_of_all_elements_located((By.ID, 'firstName')))

    # Find the text field element by it's ID, name, or other selector
    text_field = driver.find_element("name", "firstName")

    # Input text in the text field
    text_field.send_keys(accountDetailsGenerate()["first_name"])

    # Find the text field element by it's ID, name, or other selector
    text_field = driver.find_element("name", "lastName")

    # Input text in the text field
    text_field.send_keys(accountDetailsGenerate()["last_name"])

    # Find the text field element by it's ID, name, or other selector
    text_field = driver.find_element("name", "Username")

    password = accountDetailsGenerate()["password"]

    # Input text in the text field
    text_field.send_keys(accountDetailsGenerate()["username"])

    # Find the text field element by it's ID, name, or other selector
    text_field = driver.find_element("name", "Passwd")

    # Input text in the text field
    text_field.send_keys(password)

    # Find the text field element by it's ID, name, or other selector
    text_field = driver.find_element("name", "ConfirmPasswd")

    # Input text in the text field
    text_field.send_keys(password)

    # Find button to press
    button = driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ")

    # Click the button
    button.click()

    # Close the browser
    #driver.quit()

def accountDetailsGenerate():

    accountDetailsDict = {} # holds account details for each account

    # Generate random first name
    first_name = ''.join(random.choice(string.ascii_letters) for i in range(8))

    # Generate random last name
    last_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    # Generate random username
    username = ''.join(random.choice(string.ascii_lowercase + string.digits + '.') for i in range(17))

    # Generate random password
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(9))

    # populate accountDetailsDict
    accountDetailsDict["first_name"] = first_name
    accountDetailsDict["last_name"] = last_name
    accountDetailsDict["username"] = username
    accountDetailsDict["password"] = password
    
    return accountDetailsDict # returns a dictionary containing account details

#print(accountDetailsGenerate()["first_name"])

openBrowser()



