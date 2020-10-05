'''
Created on 06-Apr-2020

@author: choudaiahp
'''
from BaseTestClass import *
from Settings import *
from selenium.webdriver.support.wait import WebDriverWait


class HomepageXpath:
    def welcomeAdmin(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-header/ul/li[2]/div/span"
        
    def vendorsTab(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-header/ul/li[1]/span/a/span"
        
    def vendorVettingTitle(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-header/div/p"
        
    def plusIconVendor(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab/div/button"
        
    def Globalsearch(self):
        return "//*[@id='Grid_searchbar']" 
         
    def pagination(self):
        return "//*[@id='Grid']/div[6]/div[3]"
          
        
    def pageDropdown(self):
        return "//*[@id='Grid']/div[6]/div[7]/div[1]/span"
         