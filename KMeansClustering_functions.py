#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random
import statistics

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


def select(K):
    return 10*np.random.random((K, 2)) #creates a multi-D array of 2 elements each (k rows) 


def assign(centroids, hemoglobin, glucose):
    K = centroids.shape[0]
    distances = np.zeros((K, len(hemoglobin)))
    for i in range(K):
        g = centroids[i,1]
        h = centroids[i,0]
        distances[i] = np.sqrt((hemoglobin-h)**2+(glucose-g)**2)
    assignments = np.argmin(distances, axis = 0)
    print(assignments) 
    return assignments

 
def update(assignments, hemoglobin, glucose, centroids):
    K = centroids.shape[0]
    updatedcen = np.zeros((K, 2))
    print("cenn", updatedcen)
    count= 0
    glucsum = 0
    hemosum = 0
    for i in range(K):
        for j in range(len(assignments)):
            if i == assignments[j]:
                glucsum += glucose[j]
                hemosum += hemoglobin[j]
                count+=1
        if count != 0:
            hmean = hemosum/count
            gmean = glucsum/count
            updatedcen[i,0] = hmean
            updatedcen[i,1] = gmean
    updated_centroids = updatedcen
    print("cen", updatedcen)
    return updated_centroids
    
    
#    for i in range(len(centroids)):
#        new_dist = []
#        for index, assign in enumerate(assignments):
#            if assign == i:
#                 new_dist.append([hemoglobin[index], glucose[index]])
#        print("new dist: ", new_dist)
#    return centroids


#then walk through the centroids and find every distance that is assigned to that centroid
#then average the distance
#the average becomes the new centroid


glucose, hemoglobin, classification = openckdfile()



centroids = select(10)
assignments = assign(centroids, hemoglobin, glucose)
updated_centroids = update(assignments, hemoglobin, glucose, centroids)
print(update(assignments, hemoglobin, glucose, centroids))



plt.figure()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()
