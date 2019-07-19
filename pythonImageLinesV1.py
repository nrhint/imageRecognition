##Nathan Hinton

##TO DO:
#Recreate the picture from run 2 with the pixels gathered.

from PIL import Image, ImageFilter

filename = 'Images/4493294788823736143.jpg'
thresh = 500

run = open('runNum', 'r').read()
open('runNum', 'w').write(str(int(run)+1))

image = Image.open(filename)
image2 = Image.open(filename)

image = image.filter(ImageFilter.FIND_EDGES)
image.show()

def findWhitePix(image, thresh = 700):
    if thresh > 255*3:
        thresh = 255*3
    pixels = []
    for w in range(image.width):
        for h in range(image.height):
            pix = image.getpixel((w, h))
            total = pix[0]+pix[1]+pix[2]
            if total > thresh:
                pixels.append((w, h))
    print(pixels)
    return pixels

image = image.filter(ImageFilter.EDGE_ENHANCE)
image.show()
image.save(filename+run+'.png')
#image.show()
##print("Extracting white pixels")
##whiteExtract = findWhitePix(image, thresh)
##################################################
###Create a new image using the points that were found.
##img = Image.new('RGB', (image.width, image.height), "black")
##pixels = img.load()
##print("CreatingNewImage")
##for i in range(img.size[0]):
##    #print(i)
##    for j in range(img.size[1]):
##        if (i, j) in whiteExtract:#If the pixel is white:
##            pixels[i, j] = (255, 255, 255)
##        else:
##            pixels[i, j]= (0, 0, 0)
##image.show("basicFilter")
##img.show(title = "BlackWhiteFilter:"+str(thresh))
##



##import numpy
##from stl import mesh
##
### Using an existing stl file:
###your_mesh = mesh.Mesh.from_file('some_file.stl')
##
### Or creating a new mesh (make sure not to overwrite the `mesh` import by
### naming it `mesh`):
##VERTICE_COUNT = 100
##data = numpy.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
##your_mesh = mesh.Mesh(data, remove_empty_areas=False)
##
### The mesh normals (calculated automatically)
##your_mesh.normals
### The mesh vectors
##your_mesh.v0, your_mesh.v1, your_mesh.v2
### Accessing individual points (concatenation of v0, v1 and v2 in triplets)
##assert (your_mesh.points[0][0:3] == your_mesh.v0[0]).all()
##assert (your_mesh.points[0][3:6] == your_mesh.v1[0]).all()
##assert (your_mesh.points[0][6:9] == your_mesh.v2[0]).all()
##assert (your_mesh.points[1][0:3] == your_mesh.v0[1]).all()
##
###your_mesh.save('new_stl_file.stl')
