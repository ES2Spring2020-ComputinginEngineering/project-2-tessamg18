#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random
import statistics

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


def select(K):
    return np.random.random((K, 2)) #creates a multi-D array of 2 elements each (k rows) 


def assign(centroids, hscaled, gscaled):
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
    while iterations >= 1:
        assignments = assign(centroids, hscaled, gscaled)
        centroids = update(assignments, hscaled, gscaled, centroids)
        iterations -= 1
    return centroids
    


glucose, hemoglobin, classification = openckdfile()
hscaled = (hemoglobin-3.1)/(17.8-3.1)
gscaled = (glucose-70)/(490-70)


centroids = select(2)
assignments = assign(centroids, hscaled, gscaled)
updated_centroids = update(assignments, hscaled, gscaled, centroids)
final_centroids = iterate(20, assignments, hscaled, gscaled, centroids)


plt.figure()
plt.plot(final_centroids[:,0], centroids[:,1], "gs")
plt.plot(hscaled[classification==1],gscaled[classification==1], "k.", label = "Class 1")
plt.plot(hscaled[classification==0],gscaled[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()

plt.figure()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()
