import numpy as np

sensor = np.array([
    [20,25,30,35,40],
    [50,55,60,65,70],
    [10,15,20,25,30],
    [80,85,90,95,100]
])

mean = np.mean(sensor,axis=1)
minimum = np.min(sensor,axis=1)
maximum = np.max(sensor,axis=1)
std = np.std(sensor,axis=1)

highest = np.argmax(mean)

threshold = 60
above_threshold = sensor>threshold

print("Mean:",mean)
print("Minimum:",minimum)
print("Maximum:",maximum)
print("Standard Deviation:",std)
print("Sensor with Highest Average:",highest+1)
print("Readings Above Threshold:")
print(above_threshold)
