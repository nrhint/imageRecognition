##Nathan Hinton
##This is the collection of the bits and parts that I have made. Here will be the program that will put everything together.

##Import the packages:
from time import time as t
start = t()
print("START")
print()
print()
import numpy as np
import imutils
import cv2
from PIL import Image
import numpy2stl

#Open the image:
ratio = 5
filename = "./Photos/IMG_20190808_141950864.jpg"
print("Loading image %s"%filename)
image = cv2.imread(filename)
gray = Image.open(filename).convert('LA')
print(image.shape)
height, width = image.shape[:2]
image = cv2.resize(image, (int(width/ratio), int(height/ratio)), interpolation = cv2.INTER_AREA)

print("||")
print(image.shape)

coins = np.array(gray)
coins = coins[:, :, 0]
from skimage.data import coins
coins = coins()

markers = np.zeros_like(coins)
markers[coins < 30] = 1
markers[coins > 150] = 2
from skimage.filters import sobel
elevation_map = sobel(coins)
from skimage.morphology import watershed
segmentation = watershed(elevation_map, markers)
im = Image.fromarray(np.uint8(coins))
im.show()
im = Image.fromarray(np.uint8(elevation_map))
im.show()
im = Image.fromarray(np.uint8(segmentation))
im.show()


"""


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
"""
print()
print()
print("END")
end = t()
print("Program took %s sconds to excecute"%(end-start))
