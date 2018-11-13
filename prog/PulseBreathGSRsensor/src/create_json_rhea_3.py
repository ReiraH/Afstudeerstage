import serial
import datetime
import json
import atexit
import csv

@atexit.register
def write_to_file():
    current_time = datetime.datetime.now()
    time_now = current_time.strftime('%d_%m_%Y_%H_%M_%S')
    path = time_now + str('.json')
    with open(path, 'a') as outfile:
        json.dump(data_list, outfile)

def read_to_file():
    pass

def convert_JSON_to_CSV(_dataToCSV):
    x = _dataToCSV
    sensor = x['sensor']
    date = x['date']
    value = x['value']
    time = x['time']
    a = []
    b = []
    c = []
    i = 0

    e = csv.writer(open("all_sensors.csv", "a"),lineterminator='\n')
    e.writerow([date,
                            sensor,
                           value,
                            time])    

    if sensor == "p":
        a.append(sensor)
        f = csv.writer(open("Pulse.csv", "a"),lineterminator='\n')
        f.writerow([x['date'],
                        x['sensor'],
                        x['value'],
                        x['time']])

        print("a " + str(a))

    elif sensor == "g":
        b.append(sensor)
        g = csv.writer(open("GSR.csv", "a"),lineterminator='\n')
        g.writerow([x['date'],
                        x['sensor'],
                        x['value'],
                        x['time']])

        print("b " + str(b))

    elif sensor == "b":
        c.append(sensor)
        h = csv.writer(open("Breath.csv", "a"),lineterminator='\n')
        h.writerow([x['date'],
                        x['sensor'],
                        x['value'],
                        x['time']])

        print("c " + str(c))

    else:
        print("geen waarde gevonden")

if __name__ == "__main__":
    print("STARTING SCRIPT")

# Get ESP32 sensor data
    ser = serial.Serial('COM3', 115200, timeout=1)
    ser.flushInput()
    ser_bytes = ser.readline()
    data_list = []

    while ser_bytes:
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("ascii"))
        print(decoded_bytes)
#split op dubbele punt maakt van Pulse sensor: 1794 een array/list met 2 objecten : Pulse sensor en 1794
#pak de 2e waarde voor value oftewel 1 (met 0 meegerekent)
#value = json.loads(decoded_bytes)

# Get current time
        value = decoded_bytes.split(':')[1]
        sensor = decoded_bytes.split(':')[0]
        current_time = datetime.datetime.now()
        date_now = current_time.strftime('%d-%m-%Y')
        time_now = current_time.strftime('%H:%M:%S.%f')
        data = {
                'date': date_now,
                'time': time_now,
                'sensor': sensor,
                'value':value
            }
        convert_JSON_to_CSV(data)
        data_list.append(data)
        ser_bytes = ser.readline()