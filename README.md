
# Computer Vision I/O
This python package, Computer Vision I/O which is knwon as **_cv\_io_**, is a collection of existing python scripts which provides a set of I/O functions for normal and irregular image formats in computer vision.

## File Format Support
File format | Desciption
------------|-------------
*.png, *.jpg, ... | All normal images
*.flo | Middleburry optical flow
*.dpt | Middleburry floating point depth
*.pfm | Freiburg floating point disparity
*.exr | OpenXR hdr format
*.jxr | MicroSoft JPEG-XR hdr format


## Main Fucntions
Function | Desciption
---------|------------
imread (file\_name) | Reads an image from "file\_name"
imwrite (file\_name, image) | Saves the "image" array to "file\_name"
imshow (image) | Displays the "image" array by matplotlib
imshow (file\_name) | Displays an image file from "file\_name"

## Requirements
Package requirement are listed in [requirements.txt](requirements.txt) file and it will be installed through `pip` isntallation. If you clone the repository you may install requirements manually:

```shell
pip install -r requirements.txt
```

***
# Install as a Python Package

You can also download and install the **Simple Image Viewer** as a python package by:
```
python -m pip install cv_io
```
or simply 
```
pip install cv_io
```
Then you can simply import it in a python code and use it as follows:
```python
import cv_io
image = cv_io.imread('samples/0512.pfm')
cv_io.imshow(image)
cv_io.imwrite('test.pfm', image)
```
You also have acess to the original libraries like `sintel_io` through the `cv_io` as a sub-module: 
```python
import cv_io
image = cv_io.sintel_io.depth_read ('samples/frame_0020.dpt')
cv_io.sintel_io.depth_write('test.dpt', image)
```

***
_Copyright &copy; 2020 [Saeid Hosseinipoor](https://saeid-h.github.io/). Released under the [MIT License](LICENSE)._
