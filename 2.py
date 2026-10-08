import numpy as np

features = np.array([
    [10,100,1.5,50],
    [20,150,2.0,60],
    [30,200,2.5,70],
    [40,250,3.0,80],
    [50,300,3.5,90],
    [60,350,4.0,100],
    [70,400,4.5,110],
    [80,450,5.0,120],
    [90,500,5.5,130],
    [100,550,6.0,140]
])

mean = np.mean(features,axis=0)
std = np.std(features,axis=0)

standardized = (features-mean)/std

print("Mean:",mean)
print("Standard Deviation:",std)
print("Standardized Features:")
print(standardized)

print("New Means:",np.mean(standardized,axis=0))
print("New Standard Deviations:",np.std(standardized,axis=0))
