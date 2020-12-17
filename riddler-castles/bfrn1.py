# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:34:04 2020

@author: zsteg
"""

import csv

def throwdown(generalA,generalB):
    pointsA = []
    pointsB = []
    for castle in range(len(generalA)):
        if generalA[castle] > generalB[castle]:
            pointsA.append(castle+1)
            pointsB.append(0)
        elif generalA[castle] < generalB[castle]:
            pointsA.append(0)
            pointsB.append(castle+1)
        elif generalA[castle] == generalB[castle]:
            pointsA.append(0.5*(castle+1))
            pointsB.append(0.5*(castle+1))
        else:
            print('unexpected case!!!')
    return (pointsA,pointsB)
    
allGenerals = []

with open('castle-solutions-ZS-1.csv') as csvFile:
    reader = csv.reader(csvFile)
    next(reader)
    for row in reader:
        allGenerals.append([int(s) for s in row])




        
        
    
