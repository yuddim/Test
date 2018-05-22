#------------sceletonize with OpenCV---------------------

import cv2
import numpy as np
img = cv2.imread('sofsk.png',0)
size = np.size(img)
skel = np.zeros(img.shape,np.uint8)
ret,img = cv2.threshold(img,127,255,0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False
while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img,temp)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()
    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True
cv2.imshow("skel",skel)
cv2.waitKey(0)
cv2.destroyAllWindows()


#------------sceletonize with scikit-image-----

import matplotlib.pyplot as plt
from skimage.morphology import skeletonize, skeletonize_3d
from skimage.data import binary_blobs
import cv2
import numpy

data = cv2.imread('2_5_1.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
thresh = 127
im_bw = cv2.threshold(data, thresh, 1, cv2.THRESH_BINARY)[1]
skeleton = skeletonize(im_bw)
cv2.imshow("skeleton ",skeleton)
fig.tight_layout()
plt.show()
