import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt

local_mqttclient = mqtt.Client()
local_mqttclient.connect("Mosquitto", 1883, 60)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
img = cv.imread('..\RecognizeMe.jpg')
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#
# for (x,y,w,h) in faces:
#     cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]
#     eyes = eye_cascade.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
# cv.imshow('img',img)
# cv.waitKey(0)
# cv.destroyAllWindows()


cap = cv.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    roi_gray = None
    for (x, y, w, h) in faces:
      cv.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
      roi_gray = gray[y:y + h, x:x + w]
    # Display the resulting frame

    if roi_gray is not None :
      cv.imshow('frame', roi_gray)
      rc,png = cv.imencode('.png',roi_gray)
      msg = png.tobytes()
      local_mqttclient.publish("pictures", payload = msg,qos = 0, retain = False)
    if cv.waitKey(1) & 0xFF == ord('q'):
      break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

