import cv2
import numpy as np

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

# dst = cv2.addWeighted(img1, 0.2, img2, 0.8, 0)  # cv2混合
# dst = cv2.add(img1,img2) # cv2加法
dst = img1+img2  # np加法
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
