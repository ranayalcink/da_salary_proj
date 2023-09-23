#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 12:22:36 2022

@author: eniseranabeklen
"""


from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import time

# fetch_jobs functions takes keyword, num_pages, and location as arguments. The function opens Glassdoor on Google Chrome and uses its arguments to search jobs.

def fetch_jobs(keyword, num_pages, location):
    options = Options()
    options.add_argument("window-size=1920,1080")
    #Enter your chromedriver.exe path below
    chrome_path = r"C/Users/eniseranabeklen/Documents/GitHub/ds_salary_proj/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_path, options=options)
    driver.get("https://www.glassdoor.com/Job/index.htm")
    search_input = driver.find_element(By.ID, "KeywordSearch")
    location_input = driver.find_element(By.ID, "LocationSearch")
    location_input.clear()
    search_input.send_keys(keyword)
    location_input.send_keys(location)
    driver.find_element(By.ID, "HeroSearchButton").click()
    time.sleep(2)
    
# we are creating lists to save the scraped data.     
    company_name = []
    job_title = []
    salary_est = []
    location = []
    job_description = []
    salary_estimate = []
    company_size = []
    company_type = []
    company_sector = []
    company_industry = []
    company_founded = []
    company_revenue = []
    
    
    #Set current page to 1
    current_page = 1     
    time.sleep(3)
    
    while current_page <= num_pages:   
        
        done = False
        count = 0 
        while not done:
            #job_cards = driver.find_elements(By.XPATH, "//article[@id='MainCol']//ul/li[@data-adv-type='GENERAL']")
            
            job_cards = driver.find_elements(By.XPATH, "//li[@data-adv-type='GENERAL']")
            
            for card in job_cards:
                card.click()
                time.sleep(3)
                count += 1
                #Closes the signup prompt
                try:
                    driver.find_element(By.XPATH,".//span[@class='SVGInline modal_closeIcon']").click()
                    time.sleep(2)
                except NoSuchElementException:
                    time.sleep(2)
                    pass

                #Expands the Description section by clicking on Show More
                try:
                    driver.find_element(By.XPATH,"//*[@id='JobDescriptionContainer']/div[2]").click()
                    time.sleep(1)
                except NoSuchElementException:
                    card.click()
                    print(str(current_page) + '#ERROR: no such element')
                    driver.refresh()
                    pass
                except ElementNotInteractableException:
                    card.click()
                    driver.implicitly_wait(30)
                    driver.refresh()
                    print(str(current_page) + '#ERROR: not interactable')
                    pass

                #Scrape 
                try:
                    company_name.append(driver.find_element(By.XPATH,"//*[@id='JDCol']/div/article/div/div[1]/div/div/div/div/div[1]/div[1]/div").text)
                except:
                    company_name.append("#N/A")
                    pass

                try:
                    job_title.append(driver.find_element(By.XPATH,'//*[@id="JDCol"]/div/article/div/div[1]/div/div/div/div/div[1]/div[2]').text)
                except:
                    job_title.append("#N/A")
                    pass

                try:
                    location.append(driver.find_element(By.XPATH,'//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text)
                except:
                    location.append("#N/A")
                    pass

                try:
                    job_description.append(driver.find_element(By.XPATH,"//div[@id='JobDescriptionContainer']").text)
                except:
                    job_description.append("#N/A")
                    pass
                
                #we need to iterate through job listings to extract salary estimate data
                xpath = '//*[@id="MainCol"]/div[1]/ul/li[' + str(count) + ']/div[2]/div[3]/div[1]/span'
                try:
                    salary_estimate.append(driver.find_element(By.XPATH, xpath).text)
                except:
                    salary_estimate.append("#N/A")
                    pass
                
                try:
                    company_size.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Size']//following-sibling::*").text)
                except:
                    company_size.append("#N/A")
                    pass
                
                try:
                    company_type.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Type']//following-sibling::*").text)
                except:
                    company_type.append("#N/A")
                    pass
                    
                try:
                    company_sector.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Sector']//following-sibling::*").text)
                except:
                    company_sector.append("#N/A")
                    pass
                    
                try:
                    company_industry.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Industry']//following-sibling::*").text)
                except:
                    company_industry.append("#N/A")
                    pass
                     
                try:
                    company_founded.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Founded']//following-sibling::*").text)
                except:
                    company_founded.append("#N/A")
                    pass
                    
                try:
                    company_revenue.append(driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Revenue']//following-sibling::*").text)
                except:
                    company_revenue.append("#N/A")
                    pass

                    
                done = True
                
       # Moves to the next page         
        if done:
            print(str(current_page) + ' ' + 'out of' +' '+ str(num_pages) + ' ' + 'pages done')
            driver.find_element(By.XPATH,"//span[@alt='next-icon']").click()   
            current_page = current_page + 1
            time.sleep(4)


    driver.close()
    df = pd.DataFrame({'company': company_name, 
        'job title': job_title,
        'location': location,
        'job description': job_description,
        'salary estimate': salary_estimate,
        'company_size': company_size,
        'company_type': company_type,
        'company_sector': company_sector,
        'company_industry' : company_industry, 
        'company_founded' : company_founded, 
        'company_revenue': company_revenue})
    

    df.to_csv(keyword + '.csv')

