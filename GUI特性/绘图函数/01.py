import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
# print(img)
cv2.line(img, (0, 0), (511, 511), (0, 255, 0), 5)
cv2.rectangle(img, (10, 10), (150, 150), (0, 255, 255), 1)
cv2.circle(img, (200, 200), 50, (0, 0, 255), 3)
cv2.ellipse(img, (300, 300), (200, 100), 30, 0, 45, (60, 60, 60), -1)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# print(pts)
pts = pts.reshape((-1, 1, 2))
# print(pts)
cv2.polylines(img, [pts], False, (255, 255, 0), 2)
font = cv2.FONT_HERSHEY_COMPLEX

cv2.putText(img, 'OpenCV', (300, 300), font, 0.5, (255, 255, 255), 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
