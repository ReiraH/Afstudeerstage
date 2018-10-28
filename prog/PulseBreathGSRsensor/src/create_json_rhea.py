import serial
import datetime
import json
import atexit

@atexit.register
def write_to_file():
    current_time = datetime.datetime.now()
    time_now = current_time.strftime('%d_%m_%Y_%H_%M_%S')
    path = time_now + str('.json')
    with open(path, 'a') as outfile:
        json.dump(data_list, outfile)

def read_to_file():
    pass

if __name__ == "__main__":
    print("-----------------STARTING SCRIPT")

    # Get ESP32 sensor data
    ser = serial.Serial('COM3', 115200, timeout=1)
    ser.flushInput()
    ser_bytes = ser.readline()

    print(ser_bytes == unicode("hello\n")

    data_list = []

    while ser_bytes:
        print("-----------------STARTING JSON VULLEN")
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode('ascii').split(','))
        value = json.loads(decoded_bytes)

        print("-----------------STARTING GETTING TIJD")
        # Get current time
        current_time = datetime.datetime.now()
        date_now = current_time.strftime('%d-%m-%Y')
        time_now = current_time.strftime('%H:%M:%S')

        print("-----------------STARTING JSON TIJD")
        data = {
                'date': date_now,
                'time': time_now, 
                'value':value
            }
        
        print("-----------------STARTING JSON DATA PLAKKEN")
        data_list.append(data)
        ser_bytes = ser.readline()