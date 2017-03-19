"""
Level : Function
Dec : 双目体力视觉相机校正时，用于保存左右侧相机的帧。每个相机捕获的帧命名为left_*.jpg,right_*.jpg
Created on : 2017.03.14
Author : Iflier
"""
print(__doc__)

import cv2
import numpy as np

cam_left = cv2.VideoCapture(0)
cam_right = cv2.VideoCapture(1)
num = 0

while True:
    _, frame_left = cam_left.read()
    _, frame_right = cam_right.read()
    frame = np.hstack((frame_left, frame_right))
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xff
    if key == ord('s'):
        num += 1
        cv2.imwrite("captured_img//left_{0}.jpg".format(num), frame_left)
        cv2.imwrite("captured_img//right_{0}.jpg".format(num), frame_right)
    elif key == 27:
        break
    else:
        pass
cv2.destroyAllWindows()
cam_left.release()
cam_right.release()
