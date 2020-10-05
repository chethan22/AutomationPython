'''
Created on 06-Apr-2020

@author: choudaiahp
'''


from Test_Cases.BaseTestClass import *
from Test_Cases.Settings import *



#projectPath=getAbsolutePath('POM')
excelPath=getAbsolutePath('Test_Data')
#mPath=getAbsolutePath('Master')

class Vvlogin:

    
    def userLogin(self):
    
        print ("Opening Browser")
        #driver.maximize_window()
        
        print ("Reading Login Credentials from excel sheet")
        book=xlrd.open_workbook(os.path.join(VendorTestData))
        
        print ("Fetching Sheet Name\n")
        first_sheet = book.sheet_by_name('Login_Credentials')
        
        print("Fetching the URL, username and password from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(1,1)
        url = cell.value
        print(("vendor vetting URL is : %s." % url))
        
        cell = first_sheet.cell(2,1)
        username = cell.value
        print(("User Name is : %s." % username))
        
        cell = first_sheet.cell(3,1)
        password = cell.value
        password=int(password)
        print(("Password is : %s." % password))
        print(password)
        print ("Redirecting to specified URL\n")
        driver.maximize_window()
        driver.get(url)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/app-root/app-login/div/div/form/div[2]/div/div[2]/div/input" )))
        logo=driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/form/div[1]/img")
        if logo.is_displayed():
            print("vendor vetting Application URL Opened")
        else:
            raise Exception.message

        print ("vendor vetting Log-In page is displayed")
        
        print ("Entering User name")
        driver.find_element_by_xpath("//*[@id='userName']").send_keys(username)
        
        element.click()
        print(" clicked on password")       
        print ("Entering Password")
        element.send_keys(password)
        print ("Entered Password")
        element.send_keys(Keys.TAB)
        print ("Clicking on Sign_In button\n")
        driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/form/div[2]/div/div[3]/button").click()
        
        print ("Successfully LogIn to vendor_vetting Application")
        time.sleep(5)