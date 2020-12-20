# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:34:04 2020

@author: Zac Stegen

Code written to perform a Blotto game amongst stratigies imported from a csv.
"""

import csv
import random

def throwdown(generalA,generalB):
    """Determines the outcome of a series of battles between two generals.
    The Nth castel is worth N points. The general with the larger deployment
    recieves all of the points for a castle. If deployments are equal the
    points are split. Returns the points earned for each castle.
    
    Arguments: generalA - a list with deployments for each castle.
               generalB - a list with deployments for each castle.
               
    Returns: (pointsA, pointsB)
    
    """
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
            print('Unexpected case!!!')
    return (pointsA,pointsB)
    
def main():
        
    allGenerals = []

    with open('castle-solutions-ZS-1.csv') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            allGenerals.append([int(s) for s in row])

    allRecords = {}
    allVictories = [[0]*len(allGenerals) for general in allGenerals]
    totalVictories = [0]*len(allGenerals)

    [A,B] = sorted(random.sample(range(len(allGenerals)),2))
    (recordA, recordB) = throwdown(allGenerals[A],allGenerals[B])
    allRecords[str(A)+','+str(B)] = (recordA, recordB)

    # use sum() to dertmine winner
    if sum(recordA) > sum(recordB):
        allVictories[A][B] = 1
        totalVictories[A] += 1
    elif sum(recordB) > sum(recordA):
        allVictories[B][A] = 1
        totalVictories[B] += 1
    elif sum(recordA) == sum(recordB):
        #I don't know what to do here.
        pass
    else:
        print('Unexpected case!!!')

            
if __name__ == "__main__":
    main()
