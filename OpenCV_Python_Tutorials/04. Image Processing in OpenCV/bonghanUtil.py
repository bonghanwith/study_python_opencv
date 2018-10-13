import cv2
import numpy as np

def showImage(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)