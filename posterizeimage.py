import cv2
import numpy as np

# Load the image
image = cv2.imread("your_image.jpg")

# Define the number of levels (e.g., 4 for 4 color levels)
levels = 4
factor = 256 // levels

# Posterize the image
posterized_image = (image // factor) * factor

# Save or display the result
cv2.imwrite("posterized_image.jpg", posterized_image)
cv2.imshow("Posterized Image", posterized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
Using NumPy for Custom Posterization

Copy the code
import numpy as np
from PIL import Image

# Load the image
image = Image.open("your_image.jpg")
image_array = np.array(image)

# Define the number of levels (e.g., 6 for 6 color levels)
levels = 6
factor = 256 // levels

# Posterize the image
posterized_array = (image_array // factor) * factor
posterized_image = Image.fromarray(posterized_array.astype('uint8'))

# Save or display the result
posterized_image.save("posterized_image.jpg")
posterized_image.show()