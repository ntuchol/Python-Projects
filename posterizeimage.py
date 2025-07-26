import cv2
import numpy as np

image = cv2.imread("your_image.jpg")

levels = 4
factor = 256 

posterized_image = (image // factor) * factor

cv2.imwrite("posterized_image.jpg", posterized_image)
cv2.imshow("Posterized Image", posterized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
Using NumPy for Custom Posterization

import numpy as np
from PIL import Image

image = Image.open("your_image.jpg")
image_array = np.array(image)

levels = 6
factor = 256 

posterized_array = (image_array // factor) * factor
posterized_image = Image.fromarray(posterized_array.astype('uint8'))

posterized_image.save("posterized_image.jpg")
posterized_image.show()
