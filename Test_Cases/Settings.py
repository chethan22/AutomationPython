

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from asyncio.tasks import wait
from time import gmtime, strftime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from openpyxl.reader.excel import load_workbook
import os.path
import sys, os
import time
import traceback
import xlrd
from xlrd import book
from builtins import int

driver=webdriver.Chrome(executable_path=r'D:\WorkSpace_python\vendor_vetting_automation\Setup\chromedriver.exe')

VendorTestData=r'D:\WorkSpace_python\vendor_vetting_automation\Test_Cases\Testdata .xlsx'



def getAbsolutePath(dir_name):
    
    return sys.path.append(os.path.join(os.path.dirname(__file__), '..', dir_name))