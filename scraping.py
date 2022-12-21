# -*- coding: utf-8 -*-

"""
Created on Mon Dec 19 09:56:39 2022

@author: Joachim ANDRE

Webscrapping polluant : https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/
"""
# Import library

import pandas as pd
from selenium import webdriver
import os
import glob




# Function for data scrapping

def scrapping():
    
    # Url for scrapping

    url = "https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/2021/"
    
    # Create variable for driver

    driver = webdriver.Chrome(executable_path = "D:/programmation/Alternance/01_Le_lab_de_lendo/05_outil_diag/outil_diag_lelabdelendo/scrapping/chromedriver.exe")
    driver.get(url)
    
    b = 2

    for i in range(365):
        
        
        download_link = driver.find_element_by_xpath(f"//a[{b}]")
       
        download_link.click()
        b += 2 # Take just .csv
    
    driver.close()
    
  
# Fuction for combine multi .csv

def combine_multi_csv():
    
    # Access

    path_dowload_data = "C:/Users/joach/Downloads/"
    path_save_data = "D:/programmation/Alternance/01_Le_lab_de_lendo/05_outil_diag/outil_diag_lelabdelendo/Data/08_scrapping/"
    
    csv_files = glob.glob(path_dowload_data + "*.{}".format("csv"))
    #print(csv_files)


    df_append = pd.DataFrame()
    
    # Append all files together
    
    for file in csv_files:
        df_temp = pd.read_csv(file)
        df_append = df_append.append(df_temp, ignore_index=True)
    
    # Save as combined csv
    
    df_append.to_csv(path_save_data + 'Combined_files.csv')

scrapping()
combine_multi_csv()
