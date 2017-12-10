import cv2
import numpy as np

img = cv2.imread('1.jpg')
# 获取像素值
px = img[100, 100]
print(px)
img2 = img[61:398,67:422]
# blue = img[100, 100, 0]
# print(blue)

# 修改像素值
# img[100, 100] = [255, 255, 255]
# print(img[100, 100])

# print(img.item(100, 100, 0))
print(img.shape)
print(img.size)
print(img.dtype)
cv2.imshow('image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
