
#-*- coding:utf-8 -*-
"""
Morphologicla Transformation은 이미지를 Segmentation하여
단순화, 제거, 보정을 통해서 형태를 파악하는 목적으로 사용이 됩니다.
일반적으로 binary나 grayscale image에 사용이 됩니다. 사

용하는 방법으로는 Dilation(팽창), Erosion(침식), 그리고 2개를 조합한 Opening과 Closing이 있습니다.
여기에는 2가지 Input값이 있는데, 하나는 원본 이미지이고 또 다른 하나는 structuring element입니다.

structuring element는 원본 이미지에 적용되는 kernel입니다.
중심을 원점으로 사용할 수도 있고, 원점을 변경할 수도 있습니다.
일반적으로 꽉찬 사각형, 타원형, 십자형을 많이 사용합니다.

입력 이진 영상 : 오직 검은색(0)과 흰색(255) 화소를 포함하므로, 각 화소는 흰색이나 검은 화소 중 하나로 교체.
"""
from matplotlib import pyplot as plt
import cv2
import numpy as np


imgs = []
imgs_title = ["original", "cross_erosion", "cross_dilation","close_open", "close_close"]
imgs.append(np.array([[1,1,1,1,1,1,1],[1,1,1,1,0,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[0,1,1,1,1,1,1],[1,1,1,1,1,1,1]],dtype='f'))
#imgs.append(np.array([[1,1,1,1,1],[1,1,0,0,0],[1,1,1,0,1],[1,1,1,1,1],[1,1,1,1,1]],dtype='f'))
k_size = 3 #홀수
"""
1)Erosion
    :정의한 화소 집합(윈도우 사이즈 내)에서 찾은 최소 화소값을 현재 화소로 대치. (검정색이 최소 화소값)
"""
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(k_size,k_size))
imgs.append(cv2.erode(imgs[0],kernel,iterations = 1))

"""
2)Dilation
    : 보수 연산자로, 정의한 화소 집합에서 찾은 최대 화소값을 현재 화소로 교체.
    결과적으로 경계가 부드러워 지고, 구멍이 메꿔지는 효과를 얻을 수 있습니다.
"""
imgs.append(cv2.dilate(imgs[0],kernel,iterations = 1))

"""
3) Opening & Closing
    :Erosion과 Dilation의 조합 결과 입니다. 차이는 어느 것을 먼저 적용을 하는 차이 입니다.
    -Opeing : Erosion적용 후 Dilation 적용. 작은 Object나 돌기 제거에 적합
    -Closing : Dilation적용 후 Erosion 적용. 전체적인 윤곽 파악에 적합

"""

imgs.append(cv2.morphologyEx(imgs[0], cv2.MORPH_OPEN, kernel))
imgs.append(cv2.morphologyEx(imgs[0], cv2.MORPH_CLOSE,kernel))

for i in range(len(imgs)):
    plt.subplot(1,len(imgs),i+1),plt.imshow(imgs[i], 'gray'),plt.title(imgs_title[i])

plt.show()