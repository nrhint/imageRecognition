##Nathan Hinton

import numpy as np
#import argparse
import imutils
import cv2
from PIL import Image

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image file")
#args = vars(ap.parse_args())

filename = "test3.png"
image = Image.open(filename)

 
# load the image
image = cv2.imread(filename)
# load the image
#image = cv2.imread(args["image"])
count = []
up = 0
while len(count) == 0:
    up +=5
    # find all the 'black' shapes in the image
    lower = np.array([0, 0, 0])
    upper = np.array([up, up, up])
    shapeMask = cv2.inRange(image, lower, upper)

    # find the contours in the mask
    cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
    count = imutils.grab_contours(cnts)
    
print(up)
print("I found {} black shapes".format(len(count)))
#cv2.imshow("Mask", shapeMask)
cv2.imwrite("Mask.png", shapeMask)
 
# loop over the contours
##for c in cnts:
##	# draw the contour and show it
##	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
##	cv2.imshow("Image", image)
##	cv2.waitKey(0)
