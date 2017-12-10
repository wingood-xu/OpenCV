import cv2
import numpy as np

img = cv2.imread('1.jpg')

res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

height, width = img.shape[0:2]
res2 = cv2.resize(img, (290, 290), interpolation=cv2.INTER_CUBIC)

cv2.imshow('res', res)
cv2.imshow('img', res2)

cv2.waitKey(0)

cv2.destroyAllWindows()
