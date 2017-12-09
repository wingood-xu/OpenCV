import cv2

img = cv2.imread('1.jpg', 0)
cv2.namedWindow('meinv', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
key = cv2.waitKey(0) & 0xff

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('3.jpg', img)
