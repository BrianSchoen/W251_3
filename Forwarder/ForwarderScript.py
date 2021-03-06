import paho.mqtt.client as mqtt

print("I'm Starting Now! Oh dear god, I'm starting!!!",flush = True)

LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="pictures"

REMOTE_MQTT_HOST="CloudBroker"
REMOTE_MQTT_PORT=1885
REMOTE_MQTT_TOPIC="pictures"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc), flush = True)
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    print("Message Received", flush = True)	
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

def on_connect_remote(client, userdata, flags, rc):
        print("connected to remote broker with rc: " + str(rc), flush = True)

remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_remote
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)
remote_mqttclient.loop_start()

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message





# go into a loop
local_mqttclient.loop_forever()

  
