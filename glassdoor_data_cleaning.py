#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:45:21 2023

@author: eniseranabeklen
"""

import pandas as pd


scraper_result = pd.read_csv('data analyst.csv')

#glassdoor has a lot of duplicate job listing, to make my analysis more accurate, i deleled all the duplicates
#since we want to study salary data, i will delete rows which don't have salary values 
jobs = scraper_result.drop_duplicates(subset='job description', keep='first')
jobs = jobs[jobs['salary estimate'].notnull()]

#some salary datas contains values such as per hpur or employer est
jobs['per_hour'] = jobs['salary estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
jobs['employer_est'] = jobs['salary estimate'].apply(lambda x: 1 if 'employer est.' in x.lower() else 0)

salaries = jobs['salary estimate'].apply(lambda x: str(x).lower().replace('ca$','').replace('k','').replace('per hour', '').replace('(glassdoor est.)','').replace('(employer est.)',''))

#average salary
jobs['min_wage'] = salaries.apply(lambda x: float(x.split('-')[0]))
jobs['max_wage'] = salaries.apply(lambda x: float(x.split('-')[-1]))
jobs['min_wage'] = jobs.apply(lambda x: round(x.min_wage*2) if x.per_hour == 1 else x.min_wage, axis = 1)
jobs['max_wage'] = jobs.apply(lambda x: round(x.max_wage*2) if x.per_hour == 1 else x.max_wage, axis = 1)
jobs['average_salary'] = round((jobs.min_wage + jobs.max_wage)/2)

#creating ratings column and cleaning company names
jobs['ratings'] = jobs['company'].apply(lambda x: x[-3:] if any(chr.isdigit() for chr in x) else '')
jobs['company'] = jobs['company'].apply(lambda x: x[:-3].strip() if any(chr.isdigit() for chr in x) else x.strip())

jobs_by_location = jobs.location.value_counts() 
jobs['age'] = jobs['company_founded'].apply(lambda x: 2023 - x if x > 0 else x)

#this function take a list of keywords and look if job description values has any keywords
def tools_in_description(keywords):
    tools = pd.DataFrame()
    for i in keywords:
        jobs[str(i)] = jobs['job description'].apply(lambda x: 1 if i in x.lower() else 0)
        tools[str(i)] = jobs[i].value_counts()
    return tools
    return jobs

keywords = ['excel', 'python', 'r-studio', 'r studio', 'jupyter', 'spark', 'sql', 'qlikview', 'power bi', 'tableau', 'knime' ]
tools_table = tools_in_description(keywords)

jobs = jobs.drop('Unnamed: 0', axis='columns')

jobs.to_csv('jobs analysis.csv')
tools_table.to_csv('tools research.csv')

def title_simplifier(title):
    if 'business analyst' in title.lower():
        return 'businees analyst'
    elif 'analyst' in title.lower() and 'business analyst' not in title.lower():
        return 'analyst'
    else:
        return title.lower()
    
def seniority(title):
    if 'senior' in title.lower() or 'sr' in title.lower():
        return 'senior'
    elif 'junior' in title.lower() or 'jr' in title.lower() or 'entry' in title.lower():
        return 'junior'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'expert' in title.lower():
        return 'expert'
    else:
        return 'na'

def working_environment(description):
    if 'remote' in description.lower():
        return 'remote'
    elif 'hybrid' in description.lower():
        return 'hybrid'
    elif 'on site' in description.lower() or 'on-site' in description.lower():
        return 'on-site'
    else:
        return 'na'
    
jobs['simple_title'] = jobs['job title'].apply(title_simplifier)
jobs['simple_title'].value_counts()
jobs['seniority'] = jobs['job title'].apply(seniority)
jobs['seniority'].value_counts()
jobs['environment'] = jobs['job description'].apply(working_environment)
jobs['environment'].value_counts()
jobs['company_industry'].value_counts()

