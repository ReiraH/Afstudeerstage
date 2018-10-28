import serial
import datetime
import json

ser = serial.Serial('COM3', 115200, timeout=1)
ser.flushInput()

def writetoJSONFile(path, fileName, data):
        #eerst bestaande data ophalen uit de file
    oldData = readtoJSONFile(path,fileName, data)
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt,'w+') as json_file:
            #nieuwe data plakken aan de oudere data die al geschreven was
        oldData.append(data)
        #print(oldData)
        #weer alles schrijven in file
        json.dump(oldData, json_file)

def readtoJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt) as json_file:
        oldData = json.load(json_file)
        return oldData

#deze functie maakt van de datum een string zodat het kan omgezet worden naar JSON
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
  
path = '/'
fileName = 'example1'

while True:
    ser_bytes = ser.readline()
    if(len(ser_bytes) > 0):
           #seriele data omzetten naar een string 
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("ascii"))
        #de string omzetten naar een json object
        j = json.loads(decoded_bytes)
        #tijd toevoegen aan json object(esp32 heeft geen tijd)
        j = json.dumps({'Time':datetime.datetime.now(), 'value':j}, default = myconverter)
        print(j)
        #nog een keer omzetten naar een json object
        #pythonDictionary = json.loads(j)
        #schrijven naar de json file
        #writetoJSONFile(path, fileName, pythonDictionary)