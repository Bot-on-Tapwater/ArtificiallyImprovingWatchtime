'''Generates electronic mail addresses'''

import webbrowser # module that let's us open browser

import random # module that generates random values

import string
'''
def openBrowser(): # opens browser and the link provided

    firefox_path = "/usr/bin/firefox" # path to firefox application

    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path)) # opens firefox application

    webbrowser.get('firefox').open_new_tab('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp') # opens provided link in browser

#openBrowser() 
'''
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

print(accountDetailsGenerate())