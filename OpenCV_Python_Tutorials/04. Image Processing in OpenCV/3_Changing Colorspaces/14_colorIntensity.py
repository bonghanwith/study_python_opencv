#-*- coding:utf-8 -*-
"""

이미지 contour
: 동일한 색 또는 동일한 색상 강도를 가진 부분의 가장자리 경계를 연결한 선
정확도를 높히기 위해서 Binary Image를 사용합니다. threshold나 canny edge를 선처리로 수행합니다.
OpenCV에서는 contours를 찾는 것은 검은색 배경에서 하얀색 대상을 찾는 것과 비슷합니다.
그래서 대상은 흰색, 배경은 검은색으로 해야 합니다.

=> Find & Draw Contours
"""


import cv2
import numpy as np

img = cv2.imread('edge.jpg')

#1. 그레이 스케일로 변경
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#2. contour 대상은 흰색으로, 그외 배경은 검은색으로 변경
#threshold를 이용하여 binary image로 변환
ret, thresh = cv2.threshold(imgray,180,255,0) #contour 대상은 흰색으로, 그 외에는 검은색으로

#3. find
#contours는 point의 list형태. 예제에서는 사각형이 하나의 contours line을 구성하기 때문에 len(contours) = 1. 값은 사각형의 꼭지점 좌표.
#hierachy는 contours line의 계층 구조
#image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#4. draw
"""
cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) 
    image – 원본 이미지
    contours – contours정보.
    contourIdx – contours list type에서 몇번째 contours line을 그릴 것인지. -1 이면 전체
    color – contours line color
    thickness – contours line의 두께. 음수이면 contours line의 내부를 채움.
"""
image = cv2.drawContours(img, contours, -1, (0,255,0), 2)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()