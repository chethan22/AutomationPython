'''
Created on 09-Apr-2020

@author: choudaiahp
'''
from Test_Cases.BaseTestClass import *
from Test_Cases.Settings import *
from Test_Cases.Vvlogin import Vvlogin
from Test_Cases.VendorPageElements import VendorPageElements


class Vendorinformation:
    
    
    def verifyingVendorsSidemenu(self):
        
        vendor=VendorPageElements()
        vendor.plusIconVendor()
        print("verifying vendor information is displayed")
        vendor.vendorInformationSidemenu()
        
        print("verifying contacts is displayed in side menu")
        vendor.contactsSidemenu()
        
        print("verifying contracts is displayed in side menu")
        vendor.contractsSidemenu()
        
        print("verifying Insurances is displayed in side menu")
        vendor.insurancesSidemenu()
        
        print("verifying PandP is displayedin side menu")
        vendor.pandpSidemenu()
        
        print("verifying Financials is displayed")
        vendor.financialSidemenu()
        
        print("verifying Invoices is displayed")
        vendor.invoicesSidemenu()
        
    def verifyingVendorPopupElements(self):
        vendor=VendorPageElements()
        print("verifying the vendorname field is displayed")
        vendor.vendorname()
        
    
    def mainVendorInformation(self):
        vi=Vendorinformation()
        vi.verifyingVendorsSidemenu()
        driver.close()

if __name__ == '__main__':
    vvl=Vvlogin()
    vvl.userLogin()
    
    vi=Vendorinformation()
    vi.mainVendorInformation()