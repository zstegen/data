# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:34:04 2020

@author: zsteg
"""

import csv

allGenerals = []

with open('castle-solutions-ZS-1.csv') as csvFile:
    reader = csv.reader(csvFile)
    next(reader)
    for row in reader:
        allGenerals.append([int(s) for s in row])
    


        
        
    
