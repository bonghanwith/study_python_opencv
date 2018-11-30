#-*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

dotImage = cv2.imread('noise_2.jpg')
#holeImage = cv2.imread('images/hole_image.png')
#orig = cv2.imread('images/morph_origin.png')

#b,g,r = cv2.split(dotImage)
#dotImage = cv2.merge([r,g,b])
dotImage = cv2.cvtColor(dotImage, cv2.COLOR_BGR2GRAY)
ret1, dotImage = cv2.threshold(dotImage, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

erosion = cv2.erode(dotImage,kernel,iterations = 1)
dilation = cv2.dilate(dotImage,kernel,iterations = 1)

opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(dotImage, cv2.MORPH_CLOSE,kernel)
gradient = cv2.morphologyEx(dotImage, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(dotImage, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(dotImage, cv2.MORPH_BLACKHAT, kernel)

images =[dotImage, erosion, opening, dotImage, dilation, closing, gradient, tophat, blackhat]
titles =['Dot Image','Erosion','Opening','Dot Image', 'Dilation','Closing', 'Gradient', 'Tophat','Blackhot']

andimg = cv2.add(opening , closing)
cv2.imshow('andimg', andimg)

for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i], 'gray'),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
