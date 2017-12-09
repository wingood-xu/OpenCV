import cv2
from matplotlib import pyplot as plt

# img = cv2.imread('1.jpg')
img = plt.imread('1.jpg')
plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.imshow(img,interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
