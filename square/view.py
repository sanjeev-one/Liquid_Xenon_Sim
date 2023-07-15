import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the dimensions of your detector array
num_x = 10
num_y = 10
num_z = 21

# Initialize a 3D numpy array to hold the Edep sums
Edep_sums = np.zeros((num_x, num_y, num_z))

# Define column names
column_names = [
    "x",
    "y",
    "z",
    "Px",
    "Py",
    "Pz",
    "t",
    "PDGid",
    "EventID",
    "TrackID",
    "ParentID",
    "Weight",
    "Edep",
    "VisibleEdep",
    "Ntracks",
]

# Loop over all detectors
for x in range(num_x):
    for y in range(num_y):
        for z in range(num_z):
            # Read the file, skipping the first two rows
            df = pd.read_csv(
                f"./square/Det{x}_{y}_{z}.txt",
                skiprows=2,
                delim_whitespace=True,
                names=column_names,
            )
            df = df[df["PDGid"] == -11]

            sum_value = df["Edep"].sum()
            Edep_sums[x, y, z] = sum_value

# Now that we have the Edep sums, we can create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Create the x, y, and z coordinate arrays. We use numpy's indices to create three 3D arrays of coordinates.
x, y, z = np.indices((num_x, num_y, num_z))

# Convert the Edep sums to colors
color_values = Edep_sums / np.max(Edep_sums)
colors = plt.cm.viridis(color_values)

# Plot the scatter plot
ax.scatter(x.ravel(), y.ravel(), z.ravel(), c=colors.reshape(-1, 4), marker="o")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.title("Energy Deposited in Each Cube from positrons")
plt.show()
