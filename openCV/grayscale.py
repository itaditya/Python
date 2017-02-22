import numpy as np
import sys
# cv2 is the OpenCV library and is included via import command
import cv2
print(sys.argv[1])
# To read image me.jpg we use imread() function of cv2
img = cv2.imread('me.jpg', 0)
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
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('megray.png', img)
    cv2.destroyAllWindows()
