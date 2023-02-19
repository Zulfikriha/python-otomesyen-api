import requests

url = 'https://api-partner.krl.co.id/krlweb/v1/schedule' #endpoint target

query= {"stationid":'KPB',"timefrom":"17:00","timeto":"22:00"}

response = requests.get(url,query)

data = response.json()['data']

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
        print ("Perkiraan Berangkat" + " " + i['time_est'] + ", " "Perkiraan Sampai" + " " + i['time_est'])
        print("")
        nomor += 1