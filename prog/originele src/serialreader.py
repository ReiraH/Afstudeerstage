import serial
import datetime
import json
ser = serial.Serial('COM3', 115200, timeout=1)
ser.flushInput()
while True:
    ser_bytes = ser.readline()
    if(len(ser_bytes) > 0):
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("ascii"))
        j = json.loads(decoded_bytes)
        print(str(datetime.datetime.now()) + " // " + str(j['sensor']) + " : " + str(j['data'][0]))