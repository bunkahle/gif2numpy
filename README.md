# gif2numpy Version 1.1
Python library to convert single oder multiple frame gif images to numpy images or to OpenCV without PIL or pillow. OpenCV does not support gif images.

Install it with 

    setup.py install
    
or with

    pip install gif2numpy
    
# Usage

You can use the library this way:

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
	
There is also the class Gif inside the module which can be used to determine Gif features inside the image.
The general features are given in the dictionary image_specs.
If multiple frames are saved in the gif you can retrieve them in the list of frames. The list of exts gives
you the specifications of each frame (block_size, flags, delay_time, transparent_idx, terminator, lzw_min, 
top, left, width, height, has_color_table, local_color_table).

# Dependencies

You need to install cv2 (opencv-python), numpy, kaitaistruct by:

    pip install opencv-python numpy kaitaistruct
