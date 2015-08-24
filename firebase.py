#!/usr/bin/python
# easy_install or Pip install requests and serial package before running the programm

import serial
import time
import requests
import json

#Import Firebase URL
firebase_url = '' #<- Enter the URL of created FireBase API
 
#Connect to Serial Port for communication
ser = serial.Serial('', 9600, timeout=0) #<-Enter the Port Add. between ' ' to which Arduino is connected 
 
#Setup a loop to send Temperature values at fixed intervals

#Set Value
fixed_interval = 10 #In Seconds
 
while 1:
 try:
 #temperature value obtained from Arduino + LM35 Temp Sensor
  temperature_c = ser.readline()
 
 #current time and date
  time_hhmmss = time.strftime('%H:%M:%S')
  date_mmddyyyy = time.strftime('%d/%m/%Y')
 
 #Current location name
  temperature_location = ''; #<- Enter Location
 
  print temperature_c + ',' + time_hhmmss + ',' + date_mmddyyyy + ',' + temperature_location
 
 #Insert Record
  data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':temperature_c}
  
  result = requests.post(firebase_url + '/' + temperature_location + '/temperature.json', data=json.dumps(data))
 
 #Insert Record Module
  print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
  time.sleep(fixed_interval)
 except IOError:
  print('Something is broken!')
  time.sleep(fixed_interval)