#Please put your code for Step 2 and Step 3 in this file.
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


def graphdata(glucose, hemoglobin, classification):
#this function is meant to graph glucose vs hemoglobin
#it takes the parameters glucose, hemoglobin and classification
#it doesn't return anything, just makes a graph
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

 
def testcase():
#the purpose of this function is to generate random numbers of hemoglobin and glucose for test cases
#It does not take any paramters
#returns the new hemoglobin and new glucose numbers
    newhemoglobin = random.randint(3,18)
    newglucose = random.randint(70,490)
    return newhemoglobin, newglucose
    

def calculatedistancearray(newglucose,newhemoglobin,glucose,hemoglobin):
#the purpose of this function is to calculate the distance between newglucose,newhemoglobin 
#and the training set of glucose and hemoglobin
#it takes the parameters newglucose, newhemoglobin, glucose and hemoglobin
#it returns the distances as an array
    distance = []
    y=0
    for x in hemoglobin:
        distance.insert(y,np.sqrt( (x-newhemoglobin)**2 + (glucose[y]-newglucose)**2 ))
        y = y+1
    return distance
        

def nearestneighborclassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
#The purpose of this function is to classify the new data (test case data) as class 1 or class 0
#It takes the parameters newglucose, newhemoglobin, glucose, hemoglobin and classification
#it calls on calculatedistance and then finds the smallest distance between the new data and training set
#then the index of the minimum position is determined and the corresponding index from the classification
#array determines the classification of the new data
#returns the classification of the new data
    distance = calculatedistancearray(newglucose,newhemoglobin,glucose,hemoglobin)
    minpos = distance.index(min(distance))
    return classification[minpos]
    

def graphtestcase(newglucose,newhemoglobin, glucose, hemoglobin, classification):
#the purpose of this function is to graph the training set as well as the new data
#it takes the parameters newglucose, newhemoglobin, glucose, hemoglobin, and classification
#does not return anything
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot(newhemoglobin, newglucose, "go", label = "new data")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
    
def knearestneighborclassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
#this function determines the classification of new data based on the kth nearest points
#it calls on calculate distance and then the distances are sorted from minimum to maximum
#the first kth indices of the sorted distances are found and matched to the indices of the classification
#array which gives the classifications of the kth nearest points
#then the mode of the classifications is found, which then becomes the classification of the new data
#it returns the mode (which is the classification)
    distance = calculatedistancearray(newglucose,newhemoglobin,glucose,hemoglobin)
    sorted_indices = np.argsort(distance)
    k = sorted_indices[:k]
    k_classifications = classification[k]
    mode = statistics.mode(k_classifications)
    return mode


# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
newhemoglobin, newglucose = testcase()

hscaled = (hemoglobin-3.1)/(17.8-3.1)
gscaled = (glucose-70)/(490-70)

testcase()
graphdata(glucose, hemoglobin, classification)
graphtestcase(newglucose,newhemoglobin, glucose, hemoglobin, classification)
print(nearestneighborclassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification))
print(knearestneighborclassifier(5, newglucose, newhemoglobin, glucose, hemoglobin, classification))





