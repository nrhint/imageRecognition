##Nathan Hinton
from time import time as t
start = t()
print("START")
print()
print()
print("Importing modules...")
import numpy as np
import imutils
import cv2
from PIL import Image
import numpy2stl

ratio = 5

filename = "./square.png"
print("Loading image %s"%filename)

# load the image
image = cv2.imread(filename)
# load the image
#image = cv2.imread(args["image"])
qcount = []
up = 0
loop = True
##print("Finding quarters...")
##while loop == True:
##    x = len(qcount)
##    up += 1
##    # find all the 'black' shapes in the image
##    lower = np.array([0, 0, 0])
##    upper = np.array([up, up, up])
##    shapeMask = cv2.inRange(image, lower, upper)
##
##    # find the contours in the mask
##    cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
##            cv2.CHAIN_APPROX_SIMPLE)
##    qcount = imutils.grab_contours(cnts)
##    if up > 110:
##        loop = False
##    elif x <= len(qcount):
##        pass
##    else:
##        if len(qcount) > 2:#100:
##            pass
##        else:
##            print("Done")
##            loop = False
##
##print(image.shape)
##height, width = image.shape[:2]
##image = cv2.resize(image, (int(width/ratio), int(height/ratio)), interpolation = cv2.INTER_AREA)
##print("||")
##print(image.shape)

count = []
print("Finding the shank...")
while loop == True:
    x = len(count)
    up += 1
    # find all the 'black' shapes in the image
    lower = np.array([0, 0, 0])
    upper = np.array([up, up, up])
    shapeMask = cv2.inRange(image, lower, upper)

    # find the contours in the mask
    cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
    count = imutils.grab_contours(cnts)
    if up > 110:
        loop = False
    elif x <= len(count):
        pass
    else:
        if len(count) > 2:#100:
            pass
        else:
            print("Done")
            loop = False
#cv2.imshow('SM', shapeMask)

print("I found {} black shapes".format(len(count)))
print("Creating STL file")
numpy2stl.numpy2stl(shapeMask, "%s.stl"%filename, scale=0.05, mask_val=5., solid=False)
print("Finished with %s"%filename)
print()
print()
print("END")
end = t()
print("Program took %s sconds to excecute"%(end-start))
