from __future__ import print_function
import gif2numpy
import cv2

images = "Images/audrey.gif", "Images/hopper.gif", "Images/testcolors.gif"
for image in images:
    np_image = gif2numpy.convert(image)
    print("type of image:", image, type(np_image))
    cv2.imshow("np_image", np_image)
    cv2.waitKey()