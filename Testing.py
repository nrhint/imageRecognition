##Nathan Hinton
from time import time as t
start = t()
print("START")
print()
print()
import numpy as np
import imutils
import cv2
from PIL import Image
#import numpy2stl
from skimage import measure 

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image file")
#args = vars(ap.parse_args())

ratio = 2

filename = "test4.png"
print("Loading image %s"%filename)

# load the image
image = cv2.imread(filename)
print(image.shape)
height, width = image.shape[:2]
image = cv2.resize(image, (int(width/ratio), int(height/ratio)), interpolation = cv2.INTER_AREA)
print("||")
print(image.shape)
# load the image
#image = cv2.imread(args["image"])
count = []
up = 0
loop = True
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
        if len(count) > 100:
            pass
        else:
            print("Done")
            loop = False
    
    
print("I found {} black shapes".format(len(count)))

#Test adding dimension:
t = np.dstack(shapeMask)

verts, faces, normals, values = measure.marching_cubes_lewiner(t, 0)

faces += 1

thefile = open('test.obj', 'w')
for item in verts:
  thefile.write("v {0} {1} {2}\n".format(item[0],item[1],item[2]))

for item in normals:
  thefile.write("vn {0} {1} {2}\n".format(item[0],item[1],item[2]))

for item in faces:
  thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0],item[1],item[2]))  

thefile.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(verts[:, 0], verts[:,1], faces, verts[:, 2],
                linewidth=0.2, antialiased=True)
plt.show()
