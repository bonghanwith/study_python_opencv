import cv2 as cv
import numpy as np
import sys
sys.path.insert(0, '../common')
import bonghanUtil as u

img1 = cv.imread('../data/messi5.jpg')
img2 = cv.imread('../data/opencv-logo-white.png')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols ]

img1 = cv.imread('../data/messi5.png')
img2 = cv.imread('../data/opencv-logo-white.png')

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)

mask_inv = cv.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
