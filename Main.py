##Nathan Hinton

#Step 1: Load the template and find the calibration squares.
#Step 2: Find the shank.
from time import time
start = time()

print('Importing modules...')
from PIL import Image
import cv2
import imutils
import numpy as np

print('Loading variables...')
filename = 'template.png'
image = Image.open(filename)
width, height = image.size

def findDarkestSpot(imageIn):
    image = np.array(imageIn)
    thresh = 200
    width = 0
    height = 0
    for y in image:
        if np.amin(y) < thresh:
            height +=1
            for x in y:
                if np.amax(x)<thresh:
                    width += 1
    return(int(width/height), height)
                
print('Finding the squares...')#Use percentages to find the squares...
widthPct = int(width/5.44)
heightPct = int(height/7.04)
#Square1:
s1 = image.crop((0, 0, widthPct, heightPct))#Top left
#s1.show()
s2 = image.crop((width-widthPct, 0, width, heightPct))#Top right
#s2.show()
s3 = image.crop((0, height-heightPct, widthPct, height))#Bottom left
#s3.show()
s4 = image.crop((width-widthPct, height-heightPct, width, height))
#s4.show()
if findDarkestSpot(s1) == findDarkestSpot(s2) == findDarkestSpot(s3) == findDarkestSpot(s4):#If all squares the same:
    pass#No transform needed
else:
    print('transforming image')

################FOR TESTING###############


end = time()
print("Program took %s seconds."%(end-start))
