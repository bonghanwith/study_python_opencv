import cv2 as cv
import numpy as np
import sys

def showImage(image, title = 'result'):
    cv.imshow(title, image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1)
    
def saveImage(title, image):
    cv.imwrite(title, image)