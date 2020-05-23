'''

This python package, Computer Vision I/O which is knwon as cv_io, provides 
a set of I/O functions for normal and irregular image formats in computer vision.

# Main Fucntions
read (file_name):           Reads an image from "file_name"
save (file_name, image):    Saves the "image" array to "file_name"
show (image):               Displays the "image" array by matplotlib
show (file_name):           Displays an image file from "file_name"

# File Format Support
*.png, *.jpg, ...:  All normal images
*.flo:              Middleburry optical flow
*.dpt:              Middleburry floating point depth
*.pfm:              Freiburg floating point disparity


'''

from cv_io.collection import *