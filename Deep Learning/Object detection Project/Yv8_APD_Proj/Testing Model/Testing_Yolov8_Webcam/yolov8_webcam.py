from ultralytics import YOLO
import cv2
import math
cap=cv2.VideoCapture(0)

frame_width=int(cap.get(3))
frame_height = int(cap.get(4))

# Here 10 is the frame Speed
out=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

model=YOLO('bestS_ap_wt')

classNames = ["Aged_Person"]
while True:
    success, img = cap.read()
    # Doing detections using YOLOv8 frame by frame
    #stream = True will use the generator and it is more efficient than normal
    results=model(img,stream=True)
    #Once we have the results we can check for individual bounding boxes and see how well it performs
    # Once we have have the results we will loop through them and we will have the bounding boxes for each of the result
    # we will loop through each of the bounding box
    for r in results:
        boxes=r.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            print(x1, y1, x2, y2)
            #Since the o/p is in the form of tensor we have convert into integers by below code

            x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
            print(x1,y1,x2,y2)
            # Integer O/p

            #Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0),3)


            #print(box.conf[0]) Since confidence value will be in tensor we have to convert to integer using below code
            conf=math.ceil((box.conf[0]*100))/100
            cls=int(box.cls[0])
            class_name=classNames[cls]
            label=f'{class_name}{conf}'
            t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
            #print(t_size)
            c2 = x1 + t_size[0], y1 - t_size[1] - 3
            cv2.rectangle(img, (x1,y1), c2, [0,255,0], -1, cv2.LINE_AA)  # filled
            cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)
    out.write(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF==ord('1'):
        break
out.release()
