#-*- coding:utf-8 -*-
"""

OpenCV에서는 cv2.filter2D() 함수를 이용하여 이미지에 kernel(filter)를 적용하여 이미지를 Filtering할 수 있습니다. kernel은 행렬을 의미하는데 kernel의 크기가 크면 이미지 전체가 blur처리가 많이 됩니다. 일반적으로 5X5행렬을 아래와 같이 생성하여 적용합니다.

Filter가 적용되는 방법은

이미지의 각 pixel에 kernel을 적용합니다.
위 kernel을 예로들면 각 pixel에 5X5윈도우를 올려 놓고, 그 영역안에 포함되는 값의 Sum을 한 후에 25로 나눕니다.
그 결과는 해당 윈도우 영역안의 평균값이 되고, 그 값을 해당 pixel에 적용하는 방식입니다.

(윈도우 사이즈 내의 픽셀값들을 sum & 사이즈크기로 나누기 한 값으로 그 윈도우 전체를 변경)

"""

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('noise_eye.jpg')

cv2.namedWindow('image')
cv2.createTrackbar('K','image',1,20, nothing)

while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos('K','image')

    #(0,0)이면 에러가 발생함으로 1로 치환
    if k == 0:
        k = 1

    # trackbar에 의해서 (1,1) ~ (20,20) kernel생성
    kernel = np.ones((k,k),np.float32)/(k*k)
    dst = cv2.filter2D(img,-1,kernel)

    cv2.imshow('image',dst)

cv2.destroyAllWindows()