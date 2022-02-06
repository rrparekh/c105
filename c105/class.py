from unittest import result
import pandas as pd
import math 

#to read the csv file 
data = pd.read_csv("class2.csv")

#print(data)

#To find number of items inside the data
n = len(data)

print(n)

total = 0

#To find the mean of the data 
#To find the sum of marks 
for mark in data:
    total = total + float(mark[1])
mean = total/n
print(float(mark[1]))

#To subtract the mean from the data points and to find the square of the diffrence 
squarednumbers = []
for d in data:
    ab = int(d)-mean
    ab = ab**2
    squarednumbers.append(ab)

squaredsum = 0

for s in squarednumbers:
    squaredsum = squaredsum + s

result = squaredsum/(n-1)

sd = math.sqrt(result)

print(str(sd))