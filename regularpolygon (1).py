import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axes
fig, ax = plt.subplots(1)

# Define the center, number of vertices, and radius
center = (0.5, 0.5)
num_vertices = 6
radius = 0.3

# Create a RegularPolygon patch
polygon = patches.RegularPolygon(center, num_vertices, radius, color='blue', alpha=0.5)

# Add the patch to the axes
ax.add_patch(polygon)

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Show the plot
plt.show()