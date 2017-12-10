import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_blue = np.array([110, 50, 50])
    high_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, low_blue, high_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xff

    if k == 27:
        break

cv2.destroyAllWindows()
