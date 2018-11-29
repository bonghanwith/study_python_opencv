import cv2 as cv
import numpy as np
import sys

def showImage(image, withoutWait = True, title = 'result'):
    cv.imshow(title, image)

    if withoutWait:
        cv.waitKey(0)
        cv.destroyAllWindows()
        cv.waitKey(1)
    else:
        cv.waitKey(0)
        
def saveImage(title, image):
    cv.imwrite(title, image)
