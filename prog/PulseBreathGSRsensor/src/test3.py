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
    print("STARTING SCRIPT")

    ser = serial.Serial('COM3', 115200, timeout=1)
    ser.flushInput()
    ser_bytes = ser.readline()
    data_list = []
    print("hello")
    
currentData = ""
    while True:
        # Check to see if there is data.
        bytesToRead = ser.inWaiting()
        if (bytesToRead):
            # Read data.
            data = ser.read(bytesToRead)

            # Decode the data and add it to the current data.
            currentData += str(data.decode("ascii"))

            # Split the current data to see if there is a new line.
            result = currentData.split("\n");
            if (len(result) > 0):
                # If there is a new line that means a whole line of data has been received. Print the line.
                print(result[0])

                # Set the remainder as current data.
                currentData = result[1]