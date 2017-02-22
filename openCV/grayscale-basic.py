import numpy as np
# cv2 is the OpenCV library and is included via import command
import cv2

# To read image me.jpg we use imread() function of cv2
img = cv2.imread('messi.jpg', 0)
"""
    imread function has two params:
        1) the string with the image name i.e. 'me.jpg'
        2) the color to process on image i.e. 0 (for grayscale)
"""
# To show image we use imshow() function of cv2
cv2.imshow('image', img)
"""
    imshow function has two params:
        1) the string specifying the window title which is opened i.e. 'image'
        2) the variable which holds the processed image i.e. img
"""
k = cv2.waitKey(0)
cv2.destroyAllWindows()
