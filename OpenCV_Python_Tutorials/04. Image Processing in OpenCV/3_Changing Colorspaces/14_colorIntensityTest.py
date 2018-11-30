
import cv2
import numpy as np

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
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    canny_gary = cv2.Canny(imgray, 30, 70)
    laplacian = cv2.Laplacian(imgray, cv2.CV_8U)

    ret, thresh = cv2.threshold(imgray, 100, 255, 0)  # contour 대상은 흰색으로, 그 외에는 검은색으로
    image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.drawContours(frame, contours, -1, (0, 255, 0), 1)


    cv2.imshow('canny', canny_gary)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('Contours', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
