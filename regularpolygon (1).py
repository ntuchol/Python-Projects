import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(1)

center = (0.5, 0.5)
num_vertices = 6
radius = 0.3

polygon = patches.RegularPolygon(center, num_vertices, radius, color='blue', alpha=0.5)

ax.add_patch(polygon)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

plt.show()
