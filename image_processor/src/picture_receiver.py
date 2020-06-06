import paho.mqtt.client as mqtt
from datetime import datetime
import cv2 as cv
from PIL import Image

print("I'm Starting Now! Oh dear god, I'm starting!!!",flush = True)

f = open("/mnt/s3test/file_test.txt", "w")
f.write("Theoretical file contents")
f.close()


LOCAL_MQTT_HOST="CloudBroker"
LOCAL_MQTT_PORT=1885
LOCAL_MQTT_TOPIC="pictures"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc), flush = True)
        client.subscribe(LOCAL_MQTT_TOPIC)

	
def on_message(client,userdata, msg):
  try:
    
    # if we wanted to re-publish this message, something like this should work
    print(msg.payload, flush = True)
    #img_np = cv.imdecode(msg.payload, cv.CV_LOAD_IMAGE_COLOR)
    #picture = Image.open(img_np)
    #picture.save("/mnt/s3test/picture" + str(datetime.now()) + ".png")
    f = open("/mnt/s3test/picture" + str(datetime.now()) + ".png", "wb")
    f.write(msg.payload)
    f.close()
  except:
    print("Unexpected error:", sys.exc_info()[0], flush = True)


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message



# go into a loop
local_mqttclient.loop_forever()
