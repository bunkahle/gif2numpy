from __future__ import print_function
import gif2numpy
import cv2

print(gif2numpy.version)
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
    k = 0  
    for i in range(len(frames)):
        cv2.imshow("np_image", frames[i])
        print(exts[i])
        k = cv2.waitKey(0) 
        if k == 27: 
            break
    cv2.destroyWindow("np_image")