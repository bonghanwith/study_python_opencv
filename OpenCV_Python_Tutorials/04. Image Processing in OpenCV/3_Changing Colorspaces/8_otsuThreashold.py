#-*- coding:utf-8 -*-
"""
이미지 픽셀을 gray로 변경후, binary 이미지로 변경 시
한 픽셀의 gray_level이 임계값보다 작아서 검정색이 될 운명이다.
이 가엾은 black 픽셀들의 원래의 gray_level값을 가지고 평균 및 분산값을 구한다.
만약 픽셀 값들이 각각 천차 만별이면 분산은 거질것이고, 비슷비슷하면 분산은 작아질것이다.

흰색이 될 운명에 처한 픽셀들도 위와 동일하게 분산을 구한다.

즉 cv2.threshold 함수에서 임계값 넣어주는 것처럼
모든 임계값에 대해 각각의분산을 위와 같이 구한후, 
그중 분산 값이 제일 작은 임계값을 적용하여 이미지의 픽셀의 검/흰 운명을 정하는 방법


"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noise_eye.jpg',0)

# global thresholding
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img,(5,5),0)

ret3, th3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]

titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)', 'Original Noisy Image','Histogram',"Otsu's Thresholding", 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
	plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
	plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
	plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
	plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
	plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
	plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()