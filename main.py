#import the user class object
from classes import userClass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd






#create the user class
#import user Class Object 
#em = input("enter email please ")
#pw = input("enter pword")
#user = userClass.User(em, pw)

    
def login():
    print('''
    Have your auth ready
    Have your auth ready
    Have your auth ready
    Have your auth ready
    ''')
    driver = webdriver.Chrome()
    driver.get("https://app.respiratoryclinic.com.au/login")
    userName = driver.find_element_by_id("inputUsername")
    passWord = driver.find_element_by_id("inputPassword")
    firstSignIn = driver.find_element_by_xpath("//*[@id=\"regular-login\"]/button")
    userName.clear()
    passWord.clear()
    userName.send_keys(user.email)
    passWord.send_keys(user.password)
    firstSignIn.click()
    #enter google auth code part
    #select auth input 
    authInput = driver.find_element_by_xpath("//*[@id=\"two_factor_register_code\"]")
    authLogin = driver.find_element_by_xpath("/html/body/main/div/form/p[1]/button")

    ##need to change this so I wait for user to click login. 
    #define a function so the webdrive waits for user 
    try:
        WebDriverWait(driver,timeout=30).until(EC.url_contains("https://app.respiratoryclinic.com.au/dashboard/"))
        print("You're through")
    except:
        print("You did not login succesfully")
        return 
    

    time.sleep(10)
    

    
    
#login()

df = pd.read_csv(r'./REDRC.csv')
print(df)


