from ultralytics import YOLO
import cv2

model=YOLO('bestS_ap_wt.pt')
results=model('../images/1.jpg',show=True)

cv2.waitKey(0)

