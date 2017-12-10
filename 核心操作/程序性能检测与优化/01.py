import cv2
import numpy as np
import time

e1 = cv2.getTickCount()
time.sleep(2)
e2 = cv2.getTickCount()

time = (e2-e1)/cv2.getTickFrequency()

print(time)
print(cv2.getTickFrequency())