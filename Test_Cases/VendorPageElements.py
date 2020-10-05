'''
Created on 09-Apr-2020

@author: choudaiahp
'''
from BaseTestClass import *
from Settings import *

class VendorPageElements:
    
    def vendorInformationSidemenu(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-sider/div[1]/ul/li[1]/span/a"
        
			
    def VendorPopUpheading(self):
        return "/html/body/modal-container/div/div/div/h4/span"
        
			
    def VendorsubTab(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/ul/li[1]/a/span"
       
        
    def contactsSidemenu(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-sider/div[1]/ul/li[2]/span/a"
        
        
    def contractsSidemenu(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-sider/div[1]/ul/li[3]"
        
        
    def insurancesSidemenu(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-sider/div[1]/ul/li[4]/span/a"
        
        
    def pandpSidemenu(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-sider/div[1]/ul/li[5]/span/a"
        
        
    def financialSidemenu(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-sider/div[1]/ul/li[6]/span/a"
        
    
    
    def plusIconVendor(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab/div/button"
            
        
    def invoicesSidemenu(self):
        return "/html/body/app-root/app-headerlayout/nz-layout/nz-layout/nz-content/app-vendors/tabset/div/tab[2]/div/app-vendormenu/nz-layout/nz-sider/div[1]/ul/li[7]/span/a"
        
        
    def vendornamelabel(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[1]/label"
        
			
    def vendornamefield(self,VendorName):
        return "//*[@id='vendorname']"
        
			
    def accountNumberlabel(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[1]/label"
        
			
    def accountNumberfield(self,AccountNumber):
        return "//*[@id='accountnumber']"
        		
    def statelabel(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[2]/label"
        
			
    def stateDropdown(self,StateName):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[2]/ng-select/div/div/div[2]/input"
        
			
    def citylabel(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[2]/label"
       
			
    def cityfield(self):
        return "//*[@id='city']"
        
			
    def streetAddress1label(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[3]/label"
        
			
    def streetAddress1field(self):
        return "//*[@id='streetaddress1']"
        
			
    def streetAddress2label(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[3]/label"
        
			
    def streetAddress2field(self,StreetAddress2):
        return "//*[@id='streetaddress2']"
        
			
    def zipCodelabel(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[4]/label"
        
			
    def zipCodefield(self,ZipCode):
        return "//*[@id='zipcode']"
        
			
    def phoneNumberlabel(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[4]/label"
        
			
    def phoneNumberfiled(self,PhoneNumber):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[4]/div/input"
        
			
    def officelabel(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[5]/label"
        
			
    def officeDropdown(self,OfficeType):
        return "//html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[5]/ng-select/div/div/div[3]/input"
        
			
    def statuslabel(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[5]/label"
			
    def statusDropdown(self,VendorStatus):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[5]/ng-select/div/div/div[3]/input"
        
			
    def Faxnumberlabel(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[6]/label"
        
			
    def Faxnumberfield(self,FaxNumber):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[6]/div/input"
        
	
    def submitButton(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[2]/button"
    
    def vendorNamevalidationMsgMinchar(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[1]/div/div/div"
    
    def vendorNamevalidationMsgMaxchar(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[1]/div/div/div"
    
    def vendorNamevalidationMsgSplchar(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]"
    
    def enterVendorNamevalidationmessage(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[1]/div/div/div"
    
    def accountNumbervalidationMsgForsplchar(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[1]/div/div/div"
    
    def validationMsgforstate(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[2]/div/div"
    
    def validationmsgforstateNoitemsFound(self):
        return "//*[@id='ac09e177ffe0']/div/div[2]/div"
    
    def validationMsgForcity(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[2]/div/div/div"
    
    def validationforZipcode(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[4]/div/div/div"
    
    def validationmsgforoffice(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[1]/div[5]/div/div"
    
    def validationmsgforStatus(self):
        return "/html/body/modal-container/div/div/div/app-vendor/div/form/div/div/div/div[1]/div[2]/div[5]/div/div"
    
        		