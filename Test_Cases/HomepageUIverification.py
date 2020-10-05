'''
Created on 06-Apr-2020

@author: choudaiahp
'''
from Test_Cases.BaseTestClass import *
from Test_Cases.Settings import *
from Test_Cases.HomepageXpath import HomepageXpath



class HomepageUIverification:
    
    def homepageVerification(self):
        home=HomepageXpath()
        try:
            wait=WebDriverWait(driver,60)
            print("verifying welcome admin is displayed")
            admin=wait.until(EC.visibility_of_element_located((By.XPATH,home.welcomeAdmin())))
            print(admin.text)
            if admin.text=="Welcome Admin":
                print("welcome admin is displayed")
            else:
                raise Exception
        except Exception:
            print ("welcome admin not displayed")
            traceback.print_exc()
            raise Exception
            
        print("verifying vendortab is displayed")
              
                
            
            
            
       
        '''
            print("verifying vendortab is displayed")
            home.vendorsTab()
        
            print("verifying Title is displayed")
            home.vendorVettingTitle()
        
            print("verifying Plus icon(add vendor)in vendor page")
            home.plusIconVendor()
        
            print("verifying global search field")
            home.Globalsearch()
        
            print("Verifying the pagination is displayed")
            home.pagination()
        
            print("Verifying pagedropdown")
            home.pageDropdown()
        ''' 
        
        
       
       
       
    def mainHomepage(self):
        
            Hm=HomepageUIverification()
            Hm.homepageVerification()
            

            
            driver.close()



if __name__ == '__main__':
    vvl=BaseTestClass()
    vvl.userLogin()
    
    Hm=HomepageUIverification()
    Hm.homepageVerification()
    