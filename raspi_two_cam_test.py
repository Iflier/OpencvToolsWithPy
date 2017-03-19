"""
Level : Function
Dec : 测试相机在pi上是否可用
Created at : 2017.03.07
Author : Iflier
"""
print(__doc__)

import cv2
import numpy as np

cap_left = cv2.VideoCapture(0)
cap_right = cv2.VideoCapture(1)

while True:
    _, frame_left = cap_left.read()
    _, frame_right = cap_right.read()
    two_frame = np.hstack((frame_left, frame_right))
    cv2.imshow("Frame", two_frame)
    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
