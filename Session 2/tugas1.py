import requests
from datetime import datetime, time, timedelta

url = 'https://api-partner.krl.co.id/krlweb/v1/schedule' #endpoint target

query= {"stationid":'KPB',"timefrom":"17:00","timeto":"22:00"}

response = requests.get(url,query)

data = response.json()['data']

## get current date
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_time2 = datetime.strptime(current_time, '%H:%M:%S')

## nomor
nomor = 1
print ("==============================================================================")
print ("")
print ("Daftar Keberangkatan dari Stasiun KAMPUNG-BANDAN tujuan BEKASI Pada Jam 17.00 - 22.00")
print ("")
print ("==============================================================================")
print ("")
for i in data:
    if i['dest'] == 'BEKASI':
        print( str(nomor) + ". " + "Route Kereta " + i['route_name'])
        print ("Perkiraan Berangkat" + " " + i['time_est'] + ", " "Perkiraan Sampai" + " " + i['dest_time'])
        tiba = datetime.strptime(i['time_est'], '%H:%M:%S')
        delta = tiba - current_time2
        sec = delta.total_seconds()
        min = int(sec / 60)
        print('Akan Berangkat dalam : ' + str(min) + " menit lagi")
        print("")
        nomor += 1
