# gif2numpy
Python library to convert gif images to numpy images without PIL or pillow

Install it with 

    setup.py install
    
or with

    pip install gif2numpy
    
# Usage

You can use the library this way:

    from __future__ import print_function
    import gif2numpy
    import cv2
    
    images = "Images/audrey.gif", "Images/hopper.gif", "Images/testcolors.gif"
	for image in images:
	    np_image = gif2numpy.convert(image)
	    print("type of image:", image, type(np_image))
	    cv2.imshow("np_image", np_image)
	    cv2.waitKey()
        
There is also the class Gif inside the module which can be used to determine Gif features inside the image.
This is just the first beta version of the module - no support on special gif features or much testing has been done yet.

# TO DO:

Write more convenient function wrappers to deliver the Gif features of an image.

# Dependencies

You need to install cv2 (opencv-python), numpy, kaitaistruct by:

    pip install opencv-python numpy kaitaistruct
