# import numpy library as np
import numpy as np

# import open-cv library
import cv2

# here image is of class 'uint8', the range of values  
# that each colour component can have is [0 - 255]

# create a zero matrix of order 300x600 of 3-dimensions
image = np.zeros((300, 600, 3),np.uint8)

# fill whole pixels of dimensions
# with Blue colour.
image[:, :, 0] = 255;

# fill the pixels in range 120-180
# of row with Yellow colour
image[120:181, :, 1] = 255;
image[120:181, :, 2] = 255;
image[120:181, :, 0] = 0;

# fill the pixels in range 150 - 210 
# of coloumn with Yellow colour
image[:, 150:211, 1] = 255;
image[:, 150:211, 2] = 255;
image[:, 150:211, 0] = 0;

# Show the image formed
cv2.imshow("Sweden Flag",image);