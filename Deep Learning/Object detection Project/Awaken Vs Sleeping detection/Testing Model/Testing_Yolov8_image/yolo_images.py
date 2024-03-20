from ultralytics import YOLO
import cv2

model=YOLO('best1000s.pt')
results=model('../images/1as.jpeg',show=True)

cv2.waitKey(0)

