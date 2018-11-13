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
       
    allsensorsFile = open("all_sensors.csv", "a")
    allsensorsCSV = csv.writer(allsensorsFile, lineterminator='\n')
    allsensorsCSV.writerow(x)
    allsensorsFile.close()
    
    a = (x[0], x[1], x[4])
    b = (x[0], x[2], x[4])
    c = (x[0], x[3], x[4])

    pulseFile = open("pulse.csv", "a")
    pulseCSV = csv.writer(pulseFile, lineterminator='\n')
    pulseCSV.writerow(a)
    pulseFile.close()
    
    breathFile = open("breath.csv", "a")
    breathCSV = csv.writer(breathFile, lineterminator='\n')
    breathCSV.writerow(b)
    breathFile.close()
   
    gsrFile = open("gsr.csv", "a")
    gsrCSV = csv.writer(gsrFile, lineterminator='\n')
    gsrCSV.writerow(c)
    gsrFile.close()


if __name__ == "__main__":
    print("STARTING SCRIPT")

# Get ESP32 sensor data
    ser = serial.Serial('COM3', 115200, timeout=1)
    ser.flushInput()
    ser_bytes = ser.readline()
    data_list = []
    print("hello")
    
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
        
        _t = t.split(': ')[0]
        _p = p.split(': ')[0]
        _b = b.split(': ')[0]
        _g = g.split(': ')[0]

        #print('*' + t + '  ' + p + '  ' + b + '  ' + g + '  ' + 'd: ' + datetime_now)
        print(p + '  ' + b + '  ' + g)

        data = [t, p, b, g, datetime_now]
        data_ = [t_, p_, b_, g_, datetime_now]
        
        #print(data_)
        convert_to_CSV(data_)
        data_list.append(data)

        ser_bytes = ser.readline()