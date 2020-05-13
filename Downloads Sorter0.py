# -*- coding: utf-8 -*-
"""
@author: dahoekstra
"""

##############################################################################
###############          Import packages and set wd        ###################
import os
from os import listdir
from os.path import isfile, join
import sys
dlpath = r"c:\users\dalton\downloads"                                      # Requires input for each users directory
os.chdir(dlpath)

################# Define Relevant Variables/File Extensions ##################
pdf = ["pdf"]
excel = ["xlsx", "xls", "xlsm", "xlsb", "csv"]
word = ["docx"]
email = [".msg", "ics"]

################  Create relevant filepath directories   ######################
if not os.path.exists(dlpath + r'/PdfFiles'):
    os.chdir(dlpath)
    os.makedirs('PdfFiles')
if not os.path.exists(dlpath + r'/ExcelFiles'):
    os.chdir(dlpath)
    os.makedirs('ExcelFiles')
if not os.path.exists(dlpath + r'/WordFiles'):
    os.chdir(dlpath)
    os.makedirs('WordFiles')
if not os.path.exists(dlpath + r'/EmailFiles'):
    os.chdir(dlpath)
    os.makedirs('EmailFiles')

### iterates through the dlpath's files and returns each as an instance of "file"
file_list = [f for f in listdir(dlpath) if isfile(join(dlpath, f))]

for file in file_list:
   file2 = (dlpath + "\\" + file)
   if file2.endswith(tuple(pdf)):
       print(file2)
       os.rename(file2, dlpath + "\\PdfFiles\\" + file)
   if file2.endswith(tuple(excel)):
       print(file2)
       os.rename(file2, dlpath + "\\ExcelFiles\\" + file)
   if file2.endswith(tuple(word)):
       print(file2)
       os.rename(file2, dlpath + "\\WordFiles\\" + file)
   if file2.endswith(tuple(email)):
       print(file2)
       os.rename(file2, dlpath + "\\EmailFiles\\" + file)
