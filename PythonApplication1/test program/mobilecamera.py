"""
import urllib
import cv2
import numpy as np
import time
import urllib.request
# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.43.1:8080/shot.jpg'
while True:
    # Use urllib to get the image from the IP camera
    imgResp = urllib.request.urlopen(url)


    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)

    # Finally decode the array to OpenCV usable format ;)
    img = cv2.imdecode(imgNp,-1)


	# put the image on screen
    cv2.imshow('IPWebcam',img)
"""
#local Camera acess

import cv2
video = cv2.VideoCapture(0)
if video.isOpened():
    while True:
        check, frame = video.read()
        if check:
            cv2.imshow('Color Frame', frame)
            key = cv2.waitKey(50)
            if key == ord('q'):
                break
        else:
            print('Frame not available')
            print(video.isOpened())
