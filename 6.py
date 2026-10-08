import numpy as np

rng = np.random.default_rng(42)

data = rng.normal(50,10,1000)

mean = np.mean(data)
median = np.median(data)
std = np.std(data)
minimum = np.min(data)
maximum = np.max(data)

inside = np.sum((data>=mean-std)&(data<=mean+std))
percentage = (inside/1000)*100

print("Seed 42")
print("Mean:",mean)
print("Median:",median)
print("Standard Deviation:",std)
print("Minimum:",minimum)
print("Maximum:",maximum)
print("Percentage inside one standard deviation:",percentage)

rng = np.random.default_rng(100)

data = rng.normal(50,10,1000)

mean2 = np.mean(data)
median2 = np.median(data)
std2 = np.std(data)
minimum2 = np.min(data)
maximum2 = np.max(data)

inside2 = np.sum((data>=mean2-std2)&(data<=mean2+std2))
percentage2 = (inside2/1000)*100

print("\nSeed 100")
print("Mean:",mean2)
print("Median:",median2)
print("Standard Deviation:",std2)
print("Minimum:",minimum2)
print("Maximum:",maximum2)
print("Percentage inside one standard deviation:",percentage2)
