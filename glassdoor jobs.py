#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:57:59 2022

@author: eniseranabeklen
"""

import glassdoor_scraper as gs

results = gs.fetch_jobs('data analyst', 30, 'canada')
results
