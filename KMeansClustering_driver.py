#Please place your code for step 4 here.

import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np
import matplotlib.pyplot as plt
import random

glucose, hemoglobin, classification = kmc.openckdfile()
hscaled = (hemoglobin-3.1)/(17.8-3.1)
gscaled = (glucose-70)/(490-70)


centroids = kmc.select(3)
assignments = kmc.assign(centroids, hscaled, gscaled)
updated_centroids = kmc.update(assignments, hscaled, gscaled, centroids)
final_centroids = kmc.iterate(50, assignments, hscaled, gscaled, centroids)
kmc.graphingKMeans(glucose, hemoglobin, assignments, centroids)


plt.figure()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()

