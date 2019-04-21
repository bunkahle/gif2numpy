from __future__ import print_function
import gif2numpy
import cv2

images = "Images/Rotating_earth.gif", "Images/hopper.gif", "Images/audrey.gif", "Images/testcolors.gif"
for image in images:
    frames, exts, image_specs = gif2numpy.convert(image)
    print()
    print("Image:", image)
    print()
    print("len frames", len(frames))
    print("len exts", len(exts))
    print("exts:", exts)
    print("image_specs:", image_specs)
    for i in range(1):
        cv2.imshow("np_image", frames[i])
        cv2.waitKey(0)
    cv2.destroyWindow("np_image")