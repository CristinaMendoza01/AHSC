import pandas as pd
import numpy as np
from scipy import stats

# Load the data from the CSV file
data_file = './FullData.csv'
data = pd.read_csv(data_file)

# Select the relevant descriptors
descriptors = ['melbands_flatness_db.mean', 'spectral_centroid.mean']

# Calculate outlier bounds using interquartile range (IQR)
def calculate_outlier_bounds(data, descriptor, k=1.5):
    q1 = np.percentile(data[descriptor], 25)
    q3 = np.percentile(data[descriptor], 75)
    iqr = q3 - q1
    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr
    return lower_bound, upper_bound

# Remove outliers based on the calculated bounds
def remove_outliers(data, descriptor, lower_bound, upper_bound):
    mask = (data[descriptor] >= lower_bound) & (data[descriptor] <= upper_bound)
    return data[mask]

# Iterate over the descriptors and remove outliers
for descriptor in descriptors:
    lower_bound, upper_bound = calculate_outlier_bounds(data, descriptor)
    data = remove_outliers(data, descriptor, lower_bound, upper_bound)

# Save the cleaned data to a new CSV file
data.to_csv('cleaned_data.csv', index=False)
