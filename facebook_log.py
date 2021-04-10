from selenium import webdriver
import time

# Program to auto logg into your Facebook account

def log_web_auto(credentials, url):
    browser = webdriver.Edge(executable_path = 'msedgedriver')
    browser.get(url)
    print('The url is -> ' + browser.current_url)
    browser.implicitly_wait(10)

    username = browser.find_element_by_name('email')
    password = browser.find_element_by_name('pass')

    atts = []

    if (username and password):
        print('Name attributes were founded...')
        atts.append(username)
        atts.append(password)

    for elm in range(2):
        if elm == 1:
            atts[elm].clear()
            atts[elm].send_keys(credentials['pass'])
            break
        atts[elm].clear()
        atts[elm].send_keys(credentials['user'])

    atts[1].submit()

    return [ browser, browser.current_url ]



# If user | pass are wrong it will print: Acces Denied. Else you will be redirected to your profile
def verify_profile(browser, web):
    try:
        profile_name = browser.find_element_by_class_name('stjgntxs')
    except:
        print('Acces denied into ', web)
        browser.back()
    else:
        if (profile_name):
            return 'Succesfully logged into ' + web





# Function where we run everything
def main():
    query_email = input('Insert your email:\n')
    query_pass = input('Insert your password:\n')

    url = 'https://www.facebook.com'

    [ browser, current_url ] = log_web_auto({"user": query_email, "pass": query_pass}, url)

    print(verify_profile(browser, 'Facebook'))

    # You have 15 seconds to navigate into your account before it gets closed and the program ends
    time.sleep(15)


main()
    