"""
Level : Function
Dec : 测试相机在pi上是否可用
Created at : 2017.03.07
Author : Iflier
"""
print(__doc__)

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
