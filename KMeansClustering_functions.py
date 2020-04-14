#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random
import statistics


def openckdfile():
#The purpose of this function is to open the file with the training set
#it does not take any parameters
#it returns glucose, hemoglobin and classification as arrays
   #unpack=True makes each column an array
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


def select(K):
#The purpose of this function is to randomly select a K numbers between 0.0 and 1.0.
#It takes the parameter K, which the quantity of numbers you want to get
#these values are the initial centroids, and the function returns the random value
    return np.random.random((K, 2))


def assign(centroids, hscaled, gscaled):
#The purpose of this function is to assign all of the data points to the nearest centroid
#it takes the parameters hscaled, gscaled, and centroids
#then it returns which centroid the points are assigned to 
    K = centroids.shape[0]
    distances = np.zeros((K, len(hscaled)))
    for i in range(K):
        g = centroids[i,1]
        h = centroids[i,0]
        distances[i] = np.sqrt((hscaled-h)**2+(gscaled-g)**2)
    assignments = np.argmin(distances, axis = 0)
    print(assignments) 
    return assignments

 
def update(assignments, hscaled, gscaled, centroids):
#the purpose of this function is update the centroid to the average location of all its points
#it takes the parameters assignments, hscaled, gscaled, and centroids
#It returns the new locations of the centroids
    K = centroids.shape[0]
    updatedcen = np.zeros((K, 2))
    count= 0
    glucsum = 0
    hemosum = 0
    for i in range(K):
        for j in range(len(assignments)):
            if i == assignments[j]:
                glucsum += gscaled[j]
                hemosum += hscaled[j]
                count+=1
        if count != 0:
            hmean = hemosum/count
            gmean = glucsum/count
            updatedcen[i,0] = hmean
            updatedcen[i,1] = gmean
    updated_centroids = updatedcen
    return updated_centroids
    
    
def iterate(iterations, assignments, hscaled, gscaled, centroids):
#The purpose of this function is to continue updating the locations of the centroids
#It has the parameters iterations, assignments, hscaled, gscaled, and centroids
#It calls on the assign function and update function a specific number of times that
#is determined by the iterations
#It returns the final location of the centroids
    while iterations >= 1:
        assignments = assign(centroids, hscaled, gscaled)
        centroids = update(assignments, hscaled, gscaled, centroids)
        iterations -= 1
    return centroids


def graphingKMeans(glucose, hemoglobin, assignments, centroids):
#the purpose of this function is to graph the training data with the centroid classifications
#It takes the paramters glucose, hemoglobin, assignments, and centroids
#it does not return anything
    plt.figure()
    for i in range(assignments.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hscaled[assignments==i],gscaled[assignments==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
