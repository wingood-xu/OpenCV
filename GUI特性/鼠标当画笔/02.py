import cv2
import numpy as np


def draw_circle(event, x_pos, y_pos, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x_pos - 50, y_pos - 50), (x_pos + 50, y_pos + 50), (0, 0, 255), 1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x_pos, y_pos), 25, (255, 0, 0), 1)


img = np.zeros((255, 255, 3), np.uint8)
cv2.namedWindow('draw_circle')
cv2.setMouseCallback('draw_circle', draw_circle)

while True:
    cv2.imshow('draw_circle', img)
    if cv2.waitKey(20) & 0xff == 27:
        break

cv2.destroyAllWindows()
