import numpy as np

import cv2

image = np.zeros((300, 600, 3),np.uint8)

image[:, :, 0] = 255;

image[120:181, :, 1] = 255;
image[120:181, :, 2] = 255;
image[120:181, :, 0] = 0;

image[:, 150:211, 1] = 255;
image[:, 150:211, 2] = 255;
image[:, 150:211, 0] = 0;

cv2.imshow("Sweden Flag",image);
