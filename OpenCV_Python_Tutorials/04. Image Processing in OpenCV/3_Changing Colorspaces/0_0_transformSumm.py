
#-*- coding:utf-8 -*-
"""
1) 2d 평행이동 및 scale변환 및 회전
M = cv2.getRotationMatrix2D((cols/2, rows/2),90, 0.5)
=>cv2.warpAffine(img, M,(cols, rows))

2) affine Transformation
직선 즉 평행선을 보존하면서 이미지를 변환하며,
세개 좌표의 이동을 매개변수로 넣어 변환행렬을 구함(a,b,c) -> (a',b',c')
pts1 = np.float32([[200,100],[400,100],[200,200]])
pts2 = np.float32([[200,300],[400,200],[200,400]])
M = cv2.getAffineTransform(pts1, pts2)
=>dst = cv2.warpAffine(img, M, (cols,rows))

3) perspective Transformation
2D 평면에서 임의의 사각형을 임의의 사각형으로 매핑시킬 수 있는 변환
네개 좌표의 이동을 매개변수로 넣어 변환행렬을 구함 (a,b,c,d) -> (a',b',c',d')
pts1 = np.float32([[359,187],[359,231],[473,147],[473,194]])
pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])
M = cv2.getPerspectiveTransform(pts1, pts2)
=>dst = cv2.warpPerspective(img, M, (1100,1100))

"""