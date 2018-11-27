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
    ser = serial.Serial('COM3', 115200, timeout=1.0)
    ser.flushInput()
    ser_bytes = ser.readline()

    oudeT_ = -1
    oudeP_ = -1
    oudeB_ = -1
    oudeG = -1

    while ser_bytes:
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("ascii"))

        print(decoded_bytes)

        t = decoded_bytes.split(': ')[1]
        p = decoded_bytes.split(': ')[2]
        b = decoded_bytes.split(': ')[3]
        g = decoded_bytes.split(': ')[4]
        current_time = datetime.datetime.now()
        datetime_now = current_time.strftime('%Y-%m-%d_%H:%M:%S.%f')

        t_ = t.split(' p')[0]
        p_ = p.split(' b')[0]
        b_ = b.split(' g')[0]

        '''oudeT_ = t_
        oudeP_ = p_
        oudeB_ = b_
        oudeG = g'''

        '''update new values with old value when new value is invalid'''
        if t_ == None:
            t_ = oudeT_
        elif p_ == None:
            p_ = oudeP_
        elif b_ == None:
            b_ = oudeB_
        elif g == None:
            g = oudeG 
        else:
            pass

        '''update old values when new value is valid (bigger than 0)'''
        if t_ != None:
            oudeT_ = t_
        elif p_ == None:
            oudeP_ = p_
        elif b_ == None:
            oudeB_ = b_
        elif g == None:
            oudeG = g 
        else:
            pass


        data_ = [datetime_now, t_, p_, b_, g]

        #print(data_)
        
        convert_to_CSV(data_)
        
        ser_bytes = ser.readline()