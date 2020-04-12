#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:19:10 2020

@author: tg
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import statistics


# FUNCTIONS
def openckdfile():
#The purpose of this function is to open the file with the training set
#it does not take any parameters
#it returns glucose, hemoglobin and classification as arrays
    #unpack=True makes each column an array
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


def select(k):
    centroidh = []
    centroidg = []
    while k>=1:
        h = random.randint(3,18)
        g = random.randint(70,500)
        centroidh.append(h)
        centroidg.append(g)
        k-=1
    return centroidh, centroidg





def calculatedistancearray(centroidg,centroidh,glucose,hemoglobin):
#the purpose of this function is to calculate the distance between newglucose,newhemoglobin 
#and the training set of glucose and hemoglobin
#it takes the parameters newglucose, newhemoglobin, glucose and hemoglobin
#it returns the distances as an array
    distance = []
    y=0
    for x in hemoglobin:
        distance.insert(y,np.sqrt( (x-centroidh)**2 + (glucose[y]-centroidg)**2 ))
        y = y+1
    return distance
        

def nearestcentroidclassification(centroidg, centroidh, glucose, hemoglobin, classification):
    distance = calculatedistancearray(centroidg,centroidh,glucose,hemoglobin)
    minpos = distance.index(min(distance))
    return classification[minpos]








#def nearestcentroidclassification(centroidh, centroidg, glucose, hemoglobin):
#    distance = []
#    y=0
#    for x in hemoglobin:
#        distance.insert(y,np.sqrt( (x-centroidh)**2 + (glucose[y]-centroidg)**2 ))
#        y +=1
#    minpos = distance.index(min(distance))
#    return classification[minpos]
        

glucose, hemoglobin, classification = openckdfile()
centroidh, centroidg = select(3)

print(calculatedistancearray(centroidg,centroidh,glucose,hemoglobin))
print(nearestcentroidclassification(centroidg, centroidh, glucose, hemoglobin, classification))
#print(fuck(centroidh, centroidg ,glucose,hemoglobin, classification))

















