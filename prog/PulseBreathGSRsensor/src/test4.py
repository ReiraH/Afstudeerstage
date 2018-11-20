import serial
import datetime
import json
import atexit
import csv

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
    print(c)

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
    ser = serial.Serial('COM3', 115200, timeout=1)
    ser.flushInput()
    ser_bytes = ser.readline()
    data_list = []

    while ser_bytes:
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("ascii"))

        t = decoded_bytes.split(': ')[1]
        p = decoded_bytes.split(': ')[2]
        b = decoded_bytes.split(': ')[3]
        g = decoded_bytes.split(': ')[4]
        current_time = datetime.datetime.now()
        datetime_now = current_time.strftime('%Y-%m-%d_%H:%M:%S.%f')

        t_ = t.split(' p')[0]
        p_ = p.split(' b')[0]
        b_ = b.split(' g')[0]

        data_ = [t_, p_, b_, g, datetime_now]
        
        convert_to_CSV(data_)
        #data_list.append(data_)
        
        ser_bytes = ser.readline()