'''Generates electronic mail addresses'''

import webbrowser # module that let's us open browser

def openBrowser(): # opens browser and the link provided

    firefox_path = "/usr/bin/firefox" # path to firefox application

    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path)) # opens firefox application

    webbrowser.get('firefox').open_new_tab('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp') # opens provided link in browser

openBrowser() 