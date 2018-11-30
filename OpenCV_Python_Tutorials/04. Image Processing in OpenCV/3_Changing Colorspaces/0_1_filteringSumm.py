#-*- coding:utf-8 -*-
"""
Image Blurring은 low-pass filter를 이미지에 적용하여 얻을 수 있습니다.
고주파영역을 제거함으로써 노이즈를 제거하거나 경계선을 흐리게 할 수 있습니다.
OpenCV에는 4가지 형태의 blurring 방법을 제공하고 있습니다.


0. 일반 Filtering(평균&전체)
    : kernel 윈도우 사이즈 내의 픽셀값들을 sum & 사이즈크기로 나누기 한 값으로 그 윈도우 전체를 변경
kernel = np.ones((k,k),np.float32)/(k*k)
dst = cv2.filter2D(img,-1,kernel)

1. Averaging
    : kernel 윈도우 사이즈 내의 빅셀값들을 sum & 사이즈 크기로 나누기 한 값으로 그 윈도우 내의 중심 픽셀의 값만 변경
dst1 = cv2.blur(img,(k,k))

2. Gaussian Filtering
    :kernel 행렬의 값(윈도우 사이즈)을 Gaussian 함수를 통해서 수학적으로 생성하여 적용합니다.
    가우시안 스무딩은 신호는 보존하면서 잡음만 제거
    그러나 이 방법은 엣지 근처에서는 문제가 발생한다. (경계선까지 blur 처리가되면서 경계선이 흐려짐)
    주변 값들과 상관성이 적은 엣지 부근에서도 가우시안 스무딩은 영상을 평탄하게 만듦으로써 엣지를 없애버린다.
dst2 = cv2.GaussianBlur(img,(k,k),0)

2_1. Bilateral Filtering
    : 가우시안 필터를 수정한 방법, 양방향 필터는 약간의 연산 시간을 더 소모하지만 엣지를 보존하면서 영상의 스무딩을 수행
    경계선을 유지하면서 Gaussian Blur처리를 해주는 방법입니다.
    양방향 필터 (bilateral Filter)는 선명도를 증가시키고, 노이즈를 감소시키는 비선형 필터이다.

    bilateralFilter(src, d, sigmaColor, sigmaSpace);
    src : 입력 이미지
    d : 필터링에 이용하는 이웃한 픽셀의 지름을 정의 불가능한경우 sigmaspace 를 사용
    sigmaColor : 컬러공간의 시그마공간 정의, 클수록 이웃한 픽셀과 기준색상의 영향이 커진다
    sigmaSpace : 시그마 필터를 조정한다. 값이 클수록 긴밀하게 주변 픽셀에 영향을 미친다. d>0 이면 영향을 받지 않고, 그 외에는 d 값에 비례한다.

dst4 = cv2.bilateralFilter(img,9,75,75)


3. Median Filtering
    : kernel 윈도우 사이즈 내의 픽셀값들 중 중간 픽셀값으로 그 윈도우 전체를 변경
      ex) 윈도우 사이즈 내 픽셀값들을 크기순으로 정렬을 하면 33,54,67,84,102,163,189,212,224입니다. 이중에 중간값인 102가 중앙값으로 결정
dst3 = cv2.medianBlur(img,k)



"""
