import numpy as np

marks = np.array([
    [65,72,80,55,68],
    [45,60,52,48,50],
    [88,91,84,79,95],
    [55,62,58,64,60],
    [70,75,68,72,80],
    [40,35,48,42,45],
    [92,85,90,88,94],
    [58,54,61,57,63],
    [76,69,74,81,70],
    [49,51,46,55,52]
])

total = np.sum(marks,axis=1)
average = np.mean(marks,axis=1)
subject_average = np.mean(marks,axis=0)
highest = np.argmax(average)
count = np.sum(average>=50)
result = np.where(average>=50,"Pass","Fail")

print("Student Totals:",total)
print("Student Averages:",average)
print("Subject Averages:",subject_average)
print("Student with Highest Average:",highest+1)
print("Number of Students with Average >= 50:",count)
print("Pass/Fail:",result)
