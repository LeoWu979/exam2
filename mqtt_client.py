import paho.mqtt.client as paho
import time
import serial

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev)

# https://os.mbed.com/teams/mqtt/wiki/Using-MQTT#python-client

# MQTT broker hosted on local machine
mqttc = paho.Client()

# Settings for connection
# TODO: revise host to your IP
host = "172.20.10.2"
topic = "Mbed"

# Callbacks
def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))
"""
def on_message(mosq, obj, msg):
    print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n")
"""

def on_message(mosq, obj, msg):
    recieved_msg = str(msg.payload).split('\\')[0][2:]
    print(recieved_msg)
    str1 = recieved_msg.split(':')
    str2 = str1[1].split('#')
#    mode_str = str1[0]
    v = int(str2[1])
    if (v == 10) : 
        time.sleep(0.5)
        s.write(bytes("/Gesture/run 0 \n\r", 'UTF-8'))
 
    print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n")



def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)

# Publish messages from Python
"""
num = 0
while num != 5:
    ret = mqttc.publish(topic, "Message from Python!\n", qos=0)
    if (ret[0] != 0):
            print("Publish failed")
    mqttc.loop()
    time.sleep(1.5)
    num += 1
"""

"""
    if mode_str == 'Threshold_Angle':
        time.sleep(0.5)
        s.write(bytes("/Gesture_UI/run 0 \n\r", 'UTF-8'))
    elif mode_str == 'Tilt_Angle':
        time.sleep(0.5)
        s.write(bytes("/Tilt_Detection/run 0 \n\r", 'UTF-8'))
"""   
# Loop forever, receiving messages
mqttc.loop_forever()