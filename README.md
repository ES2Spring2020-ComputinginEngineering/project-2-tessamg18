This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).
FUNCTION OVERVIEW:

FUNCTIONS IN NEAREST NEIGHBOR CLASSIFIER FILE
openckdfile
  takes no arguments
  opens the ckd file and returns glucose, hemoglobin, and classification as arrays

graphdata
  the parameters are glucose, hemoglobin, and classification
  this function graphs the training set data
  it does not return anything

testcase
  takes no arguments
  this function generates random numbers for hemoglobin and glucose for test cases
  it returns the random hemoglobin and glucose values

calculatedistancearray
  the paramters are newglucose, newhemoglobin, glucose and hemoglobin
  this function calculates the distance between newglucose/newhemoglobin and the training set data
  it returns the distances

nearestneighborclassifier
  the parameters are newglucose, newhemoglobin, glucose, hemoglobin, and classification
  this function classifies the test case as class 1 or class 0
  it returns the classification

graphtestcase
  the parameters are newglucose, newhemoglobin, glucose, hemoglobin, and classification
  this function graphs the training set as well as the test case
  it does not return anything

knearestneighborclassifier
  the parameters are k, newglucose, newhemoglobin, glucose, hemoglobin, and classification
  this function determines the classification of new data based on the k nearest points
  it returns the classification
  
  
FUNCTIONS IN K-MEANS CLUSTERING FUNCTIONS FILE
openckdfile
 takes no arguments
  opens the ckd file and returns glucose, hemoglobin, and classification as arrays
  
select
  the parameter is k
  this function randomly selects k numbers between 0.0 and 1.0
  it returns the random values
  
assign
  the paramters are centroids, hscaled, and gscaled
  this function assigns all of the data points to the nearest centroid
  it returns the assignments of the data points
  
update
  the paramters are assignments, hscaled, gscaled, and centroids
  this function updates the location of the centroid to the average of all of its assigned points
  it returns the updated location
  
iterate
  the parameters are iterations, assignments, hscaled, gscaled, and centroids
  this function continues updating the location(s) of the centroid(s)
  it returns the final location(s) of the centroid(s)
  
graphingKMeans
  the parameters are glucose, hemoglobin, assignments, and centroids
  this function graphs the training data with the centroid classifications
  it does not return anything
