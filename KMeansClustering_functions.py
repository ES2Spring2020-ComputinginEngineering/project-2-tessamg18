#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random
import statistics

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def select(K):
    return np.random.random((K, 2))

def assign(centroids, hemoglobin, glucose):
    K = centroids.shape[0]
    distances = np.zeros((K, len(hemoglobin)))
    for i in range(K):
        g = centroids[i,1]
        h = centroids[i,0]
        distances[i] = np.sqrt((hemoglobin-h)**2+(glucose-g)**2)
    assignments = np.argmin(distances, axis = 0)    
    print(assignments)
    return None

def update(assignments, hemoglobin, glucose, centroids):
    sortassignments = np.argsort(assignments)
    K = centroids.shape[0]
    updatedcen = np.zeros((K, 2))
    for i in range(K):
        if sortassignments == i:
            updatedcen[10] = np.mean(glucose[sortassignments==i])
            updatedcen[i] = np.mean(hemoglobin[sortassignments==i])
    return updatedcen


glucose, hemoglobin, classification = openckdfile()

plt.figure()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()


centroids = select(10)
assignments = assign(centroids, hemoglobin, glucose)
print(update(assignments, hemoglobin, glucose, centroids))
