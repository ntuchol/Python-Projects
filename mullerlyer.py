import matplotlib.pyplot as plt

def draw_muller_lyer(length, arrow_size):
  """Draws the Müller-Lyer illusion.

  Args:
    length: The length of the lines.
    arrow_size: The size of the arrows.
  """
  plt.figure(figsize=(8, 4))

  # Line with outward-pointing arrows
  plt.subplot(1, 2, 1)
  plt.plot([0, length], [0, 0], 'k-')
  plt.plot([0, arrow_size], [0, arrow_size], 'k-')
  plt.plot([0, arrow_size], [0, -arrow_size], 'k-')
  plt.plot([length, length - arrow_size], [0, arrow_size], 'k-')
  plt.plot([length, length - arrow_size], [0, -arrow_size], 'k-')
  plt.title("Outward Arrows")
  plt.axis('off')
  plt.xlim([-arrow_size, length + arrow_size])
  plt.ylim([-arrow_size * 2, arrow_size * 2])

  # Line with inward-pointing arrows
  plt.subplot(1, 2, 2)
  plt.plot([0, length], [0, 0], 'k-')
  plt.plot([0, arrow_size], [arrow_size, 0], 'k-')
  plt.plot([0, arrow_size], [-arrow_size, 0], 'k-')
  plt.plot([length, length - arrow_size], [arrow_size, 0], 'k-')
  plt.plot([length, length - arrow_size], [-arrow_size, 0], 'k-')
  plt.title("Inward Arrows")
  plt.axis('off')
  plt.xlim([-arrow_size, length + arrow_size])
  plt.ylim([-arrow_size * 2, arrow_size * 2])

  plt.show()

# Example usage:
draw_muller_lyer(10, 1)