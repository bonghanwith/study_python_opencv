import numpy as np
import cv2 as cv
import bonghanUtil as util

img  = cv.imread('blox.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

surf = cv.xfeatures2d.SURF_create(10000)
kp, des = surf.detectAndCompute(gray, None)
#img  = cv.drawKeypoints(gray, kp, img)
#img  = cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#img  = cv.drawKeypoints(gray,kp,img)
img2  = cv.drawKeypoints(gray, kp, img, (255, 0, 0), 4)
print(len(kp))
util.showImage(img)

