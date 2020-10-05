'''
Created on 06-Apr-2020

@author: choudaiahp
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
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


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="D:\WorkSpace_python\Demo\chromedriver.exe")

def getAbsolutePath(dir_name):
    
    return sys.path.append(os.path.join(os.path.dirname(__file__), '..', dir_name))