from ultralytics import YOLO
import cv2
import math
import pygame

# Initialize Pygame for audio playback
pygame.mixer.init()

cap = cv2.VideoCapture('../videos/1.mp4')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

model = YOLO('best1000s.pt')

classNames = ["Awaken", "Sleeping"]

# Load the audio files
awaken_audio = pygame.mixer.Sound('Alert2.wav')  # Adjust filename as needed

# Flag to track if "Awaken" class is detected
awaken_detected = False

while True:
    success, img = cap.read()

    # Doing detections using YOLOv8 frame by frame
    results = model(img, stream=True)

    awaken_detected = False  # Reset the flag for each frame

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Check if confidence is above 90 percent
            conf = math.ceil((box.conf[0] * 100)) / 100
            if conf >= 0.90:
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)  # filled
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

                if class_name == "Awaken":
                    awaken_detected = True

    out.write(img)
    cv2.imshow("Image", img)

    # If "Awaken" class is detected and music is not already playing, play the awaken audio
    if awaken_detected and not pygame.mixer.get_busy():
        awaken_audio.play()
    elif not awaken_detected:
        pygame.mixer.stop()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
