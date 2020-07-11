import numpy as np
from mtcnn.mtcnn import MTCNN
import cv2 as cv

cap = cv.VideoCapture(0)
model = MTCNN()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = model.detect_faces(frame)
    roi_frame = None
    for face in faces:
        x, y, w, h = face['box']
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_frame = frame[y:y + h, x:x + w]
    # Display the resulting frame

    if roi_frame is not None :
      cv.imshow('window', frame)
      rc,png = cv.imencode('.png',roi_frame)
      msg = png.tobytes()
      # local_mqttclient.publish("pictures", payload = msg,qos = 0, retain = False)
    if cv.waitKey(1) & 0xFF == ord('q'):
      break
