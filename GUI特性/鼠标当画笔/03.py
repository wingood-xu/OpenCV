import numpy as np
import cv2

drawing = False
mode = True

ix = -1
iy = -1


def draw(event, x, y, flags, parame):
    global drawing, mode, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing is True:
            if mode is True:
                cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
            else:
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow('draw')
cv2.setMouseCallback('draw', draw)

while True:
    cv2.imshow('draw', img)
    k = cv2.waitKey(1) & 0xff

    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
