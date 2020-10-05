'''
Created on 15-Apr-2020

@author: choudaiahp
'''
from BaseTestClass import *
from Settings import *

class ContactsPageElements:
    
    def globalsearch(self):
        return "//*[@id='Grid_searchbar'']"
    
    def cotactsTab(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-layout/div/app-contacts/tabset/ul/li/a/span"
    
    def plusIcon(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-layout/div/app-contacts/tabset/div/tab/div/button"
    
    def firstNamefilter(self):
        return "//*[@id='firstname_filterBarcell'']"
    
    def lastNameFilter(self):
        return "//*[@id='lastname_filterBarcell']"
    
    def faxFilter(self):
        return "//*[@id='fax_filterBarcell']"
    
    def emailfilter(self):
        return "//*[@id='email_filterBarcell']"
    
    def phoneNumberfilter(self):
        return "//*[@id='phone_filterBarcell']"
    
    def statusFilter(self):
        return "//*[@id='statusId_filterBarcell']"
    
    def firstcontactInTable(self):
        return "//*[@id='Grid_content_table']/tbody/tr/td[1]/a"
    
    def itemsperPageDropDown(self):
        return "//*[@id='Grid']/div[6]/div[7]/div[1]/span"
    
    def sidemenuUnexpand(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-sider/div[2]/i"
    
    
    
    
    