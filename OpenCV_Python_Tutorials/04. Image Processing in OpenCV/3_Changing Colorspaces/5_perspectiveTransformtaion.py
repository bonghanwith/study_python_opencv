#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Homography를 직관적으로 이해하기 위한 한 좋은 방법은 
2D 평면에서 임의의 사각형을 임의의 사각형으로 매핑시킬 수 있는 변환이 
homography다 라고 생각하는 것
"""

img = cv2.imread('harley_quinn.jpg')
# [x,y] 좌표점을 4x2의 행렬로 작성
# 좌표점은 좌상->좌하->우상->우하
pts1 = np.float32([[359,187],[359,231],[473,147],[473,194]])

# 좌표의 이동점
pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])

# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.
cv2.circle(img, (504,1003), 20, (255,0,0),-1)
cv2.circle(img, (243,1524), 20, (0,255,0),-1)
cv2.circle(img, (1000,1000), 20, (0,0,255),-1)
cv2.circle(img, (1280,1685), 20, (0,0,0),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (1100,1100))

plt.subplot(121),plt.imshow(img),plt.title('image')
plt.subplot(122),plt.imshow(dst),plt.title('Perspective')
plt.show()