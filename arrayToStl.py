##Nathan Hinton
##This is for writing an array to a stl file

input('name: ')

data = 'solid %s\n'%name

#Add data in the format of:
'''
facet normal nx ny nz
    outer loop
        vertex v1x v1y v1z
        vertex v2x v2y v2z
        vertex v3x v3y v3z
    endloop
endfacet
'''

