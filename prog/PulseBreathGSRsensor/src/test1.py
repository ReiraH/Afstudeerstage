import serial
import datetime
import json
import atexit
import csv

'''
@atexit.register
def write_to_file():
    current_time = datetime.datetime.now()
    time_now = current_time.strftime('%d_%m_%Y_%H_%M_%S')
    path = time_now + str('.json')
    convert_JSON_to_CSV(data_list)
    with open(path, 'a') as outfile:
        json.dump(data_list, outfile)
'''

def read_to_file():
    pass

def convert_to_CSV(_dataToCSV):
    x = _dataToCSV
    
    f = csv.writer(open("all_sensors.csv", "a"),lineterminator='\n')
    #f.writerow(["time", "pulse", "breath", "gsr", "datetime"])

    f.writerow([x]) 


if __name__ == "__main__":
    print("STARTING SCRIPT")

# Get ESP32 sensor data
    ser = serial.Serial('COM3', 115200, timeout=1)
    ser.flushInput()
    ser_bytes = ser.readline()
    data_list = []
    
    while ser_bytes:
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("ascii"))
        #print(decoded_bytes)

        t = decoded_bytes.split('  ')[0]
        p = decoded_bytes.split('  ')[1]
        b = decoded_bytes.split('  ')[2]
        g = decoded_bytes.split('  ')[3]
        current_time = datetime.datetime.now()
        datetime_now = current_time.strftime('%Y-%m-%d_%H:%M:%S.%f')

        t_ = t.split(': ')[1]
        p_ = p.split(': ')[1]
        b_ = b.split(': ')[1]
        g_ = g.split(': ')[1]

        #print('*' + t + '  ' + p + '  ' + b + '  ' + g + '  ' + 'd: ' + datetime_now)
        

        data = {t, p, b, g, datetime_now}
        data_ = {t_, p_, b_, g_, datetime_now}
        
        import numpy as np
        myarray = np.asarray(data_)

        print(myarray)
        convert_to_CSV(myarray)
        data_list.append(data)

        ser_bytes = ser.readline()