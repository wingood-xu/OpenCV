import numpy as np
import cv2


def nothing(x):
    print(x)


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('color')
cv2.createTrackbar('R', 'color', 0, 255, nothing)
cv2.createTrackbar('G', 'color', 0, 255, nothing)
cv2.createTrackbar('B', 'color', 0, 255, nothing)

switch = '0:OFF\n1:on'
cv2.createTrackbar(switch, 'color', 0, 1, nothing)

while True:
    cv2.imshow('color', img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

    r = cv2.getTrackbarPos('R', 'color')
    g = cv2.getTrackbarPos('G', 'color')
    b = cv2.getTrackbarPos('B', 'color')

    s = cv2.getTrackbarPos(switch, 'color')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv2.destroyAllWindows()
