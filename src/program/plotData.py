import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Read CSV file
data_file = './FullData.csv'
data = pd.read_csv(data_file)

# Select all columns except the last one
cols = data.columns[:-1]

# Create a neew DatFrame with the selected columns
data_sel = data[cols]

# Apply PCA to reduce to 2D
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data_sel)

# Create plot
fig, ax = plt.subplots()

ax.scatter(reduced_data[:, 0], reduced_data[:, 1])

plt.show()
