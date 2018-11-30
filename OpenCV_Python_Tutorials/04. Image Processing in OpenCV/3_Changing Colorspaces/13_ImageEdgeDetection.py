#-*- coding:utf-8 -*-
"""
OpenCV는 Sobel, Scharr 및 Laplacian, canny 의 세 가지 유형의 그래디언트 필터 또는 하이 패스 필터를 제공
Gradient를 이용해서 이미지의 edge를 검출하는 방법

1) Sobel & Scharr Filter
:Gaussian smoothing과 1차 미분을 기반으로 한 유명한 엣지 검출 방법이다.
X축과 Y축을 미분하는 방법으로 경계값을 계산하며, X축 미분은 수평선(수직선이 남음), Y축 미분은 수직선(수평선이 남음)을 미분하여 경계가 사라지는 효과가 있습니다.

    1. 수직 엣지 검출 (|)
    [-1, 0, 1]
    [-2, 0, 2]
    [-1, 0 ,1]

    2. 수평 엣지 검출 (-)
    [-1, -2, -1]
    [0,   0,  0]
    [1,   2,  1]

    3. 대각 엣지 검출 (\)
    [0,  1, 2]
    [-1, 0, 1]
    [-2, -1,0]

    4. 대각 엣지 검출 2 (/)
    [-2, -1, 0]
    [-1,  0, 1]
    [0,   1, 2]

2) Laplacian 함수
: 이미지의 가로와 세로에 대한 Gradient를 2차 미분한 값입니다. Sobel filter에 미분의 정도가 더해진 것과 비슷합니다.
먼저 2D 가우시안 함수(공식 1)를 사용하여 이미지를 블러시킨다. 노이즈를 제거 및 완화시키기 위함이다. 노이즈를 엣지로 착각할 수 있기 때문이다.

LoG 연산의 알고리즘을 정리해보자.
1. gaussian 필터 처리해서 블러된 이미지를 얻는다. (노이즈 제거)
2. 블러된 이미지를 라플라시안 마스크로 컨볼루션해주면 엣지 영상을 얻을 수 있다.


3) Canny Edge Detection
: 장 유명한 Edge Detection방법입니다. 여러 단계의 Algorithm을 통해서 경계를 찾아 냅니다.
기본적으로 그레이스케일화 된 이미지만 처리 가능.

canny 기법 정리해보자.
1. gaussian 필터 처리해서 블러된 이미지를 얻는다. (노이즈 제거)
2. sobel 커널을 수평, 수직 방향으로 적용으로 gradient(x,y) 획득
    (gradient 방향은 에지에 수직인 방향)
3. 최대값이 아닌 픽셀의 값은 0으로 만들기
   이미지 전체를 스캔하여 gradient 방향으로 픽셀을 검사하면서 gradient 방향에 있는 필셀들중 특정 픽셀의
   gradient 값이 가장 크면 그대로 두고 다음으로 넘어가고, 그렇지 않으면 픽셀값을 0으로 만듬
4. 3단계 완료 후 실제로 남은 픽셀들이 엣지인지 판단하는 단계
    minVal, maxVal 2개를 잡은 후, maxVal보다 높은 부분은 확실한 엣지이고
    minVal보다 낮은 부분은 엣지가 아니라 판단.

"""


import cv2
import numpy as np
from matplotlib import pyplot as plt


# the number to specify which camera
# also you can playing video from file, : cap = cv2.VideoCapture('vtest.avi')
cap = cv2.VideoCapture(0)

#frame width by cap.get(3)
#change width
ret = cap.set(3, 320)

#frame height by cap.get(4)
#change height
ret = cap.set(4, 240)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    canny_gary = cv2.Canny(gray, 30, 70)
    laplacian = cv2.Laplacian(gray, cv2.CV_8U)

    cv2.imshow('frame', gray)
    cv2.imshow('canny', canny_gary)
    cv2.imshow('laplacian', laplacian)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

"""
# example source code

img = cv2.imread('edge.jpg', 0)
canny = cv2.Canny(img,30,70)

laplacian = cv2.Laplacian(img,cv2.CV_8U)
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

images = [img,laplacian, sobelx, sobely, canny]
titles = ['Origianl', 'Laplacian', 'Sobel X', 'Sobel Y','Canny']

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i], 'gray'),plt.title([titles[i]])
    plt.xticks([]),plt.yticks([])

plt.show()
"""
