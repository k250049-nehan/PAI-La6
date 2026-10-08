import numpy as np

image = np.array([
    [20,50,80,120,150],
    [30,70,100,140,180],
    [40,90,130,170,200],
    [50,110,150,190,220],
    [60,125,160,210,255]
])

minimum = np.min(image)
maximum = np.max(image)
mean = np.mean(image)

threshold = 128

mask = image>threshold
thresholded = np.where(image>threshold,255,0)

print("Minimum Intensity:",minimum)
print("Maximum Intensity:",maximum)
print("Mean Intensity:",mean)
print("Binary Mask:")
print(mask)
print("Thresholded Image:")
print(thresholded)
