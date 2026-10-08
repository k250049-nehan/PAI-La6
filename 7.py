import numpy as np

data = np.array([
    10,
    20,
    np.nan,
    30,
    40,
    np.nan,
    50,
    60
])

nan_values = np.isnan(data)

mean = np.nanmean(data)
minimum = np.nanmin(data)
maximum = np.nanmax(data)
std = np.nanstd(data)

data = np.where(np.isnan(data),mean,data)

print("NaN Locations:",nan_values)
print("Mean:",mean)
print("Minimum:",minimum)
print("Maximum:",maximum)
print("Standard Deviation:",std)
print("Data after replacing NaN:",data)
print("Any NaN remaining:",np.isnan(data).any())
