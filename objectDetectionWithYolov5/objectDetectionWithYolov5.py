import cv2
import torch
import numpy as np
import time
import pandas

path = 'best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)

cap = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0


while True:
  ret, frame = cap.read()
  results=model(frame)
  frame= np.squeeze(results.render())

  a = results.pandas().xyxy[0].values.flatten().tolist()

  if len(a) > 0:
    xmin = a[0]
    ymin = a[1]
    xmax = a[2]
    ymax = a[3]
    print(f"xmin: {xmin} ymin: {ymin} xmax: {xmax} ymax: {ymax}")

    cx = int((xmax + xmin) / 2)
    cy = int((ymin + ymax) / 2)

    cv2.circle(frame, (cx, cy), 3, (0, 255, 0), 3)
    #center of object

  cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  font = cv2.FONT_HERSHEY_SIMPLEX
  new_frame_time = time.time()
  fps = 1/(new_frame_time-prev_frame_time)
  prev_frame_time = new_frame_time

  fps = int(fps)
  fps = str(fps)

  cv2.putText(frame,fps,(7,70),font,3,(210,35,35),3,cv2.LINE_AA)#fps

  cv2.imshow("Frame",frame)
  
  if cv2.waitKey(1) & 0xff==27:
    break

cap.release()
cv2.destroyAllWindows()