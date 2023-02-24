import requests
from datetime import datetime, time, timedelta

def apiKRL(stasiun,berangkat,tiba):
    url = f'https://api-partner.krl.co.id/krlweb/v1/schedule?stationid={stasiun}&timefrom={berangkat}&timeto={tiba}'
    response = requests.get(url)
    data1 = response.json()['data']
    return data1

##call function
getkrl = apiKRL('KPB','17:00','23:00')

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
for i in getkrl:
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
