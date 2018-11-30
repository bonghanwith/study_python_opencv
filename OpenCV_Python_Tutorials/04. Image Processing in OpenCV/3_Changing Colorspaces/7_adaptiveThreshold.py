#-*- coding:utf-8 -*-
"""
이전 Section에서의 결과를 보면 한가지 문제점이 있습니다.
임계값을 이미지 전체에 적용하여 처리하기 때문에 하나의 이미지에 음영이 다르면
일부 영역이 모두 흰색 또는 검정색으로 보여지게 됩니다.

이런 문제를 해결하기 위해서 이미지의 작은 영역별로 thresholding을 하는 것입니다.
이때 사용하는 함수가 cv2.adaptiveThreshold() 입니다.

global Threshold는 문턱 값을 하나의 이미지 전체에 적용시키는 반면
adaptive Threshold는 이미지의 구역구역마다 threshold를 실행 시켜주는 것이다.

adaptive method: 사용할 문턱값 계산 알고리즘

cv2.ADAPTIVE_THRESH_MEAN_C: X, Y를 중심으로 block Size * block Size 안에 있는 픽셀 값의 평균에서 C를 뺸 값을 문턱값으로 함
cv2.ADAPTIVE_THRESH_GAUSSIAN_C: X, Y를 중심으로 block Size * block Size 안에 있는 Gaussian 윈도우 기반 가중치들의 합에서 C를 뺀 값을 문턱값으로 한다.

blocksize: block * block size에 각각 다른 문턱값이 적용된다.
C: 보정 상수로서 adaptive에 계산된 값에서 양수면 빼주고 음수면 더해준다.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('harley_quinn.jpg',0)
# img = cv2.medianBlur(img,5)

ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)



th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,15,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,15,2)

titles = ['Original','Global','Mean','Gaussian']

images = [img,th1,th2,th3]

for i in range(4):
	plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()