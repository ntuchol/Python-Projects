import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(1)

circle = patches.Circle((0.5, 0.5), 0.2, facecolor='lightcoral', edgecolor='red')
ax.add_patch(circle)

rect = patches.Rectangle((0.2, 0.2), 0.5, 0.3, facecolor='lightblue', edgecolor='blue')
ax.add_patch(rect)

polygon = patches.Polygon([(0.2, 0.2), (0.8, 0.2), (0.5, 0.8)], facecolor='lightgreen', edgecolor='green')
ax.add_patch(polygon)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')
plt.title('Drawing Shapes in Matplotlib')
plt.grid(True)
plt.show()
