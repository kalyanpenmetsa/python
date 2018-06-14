import urllib
import json
import sqlite3
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

conn = sqlite3.connect('geodb.sqlite')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Geodata')
cursor.execute('CREATE TABLE Geodata(place VARCHAR(128), Address VARCHAR(128), Lat VARCHAR(128), Long VARCHAR(128), County VARCHAR(128), City VARCHAR(128))')

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

#    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    cou = js["results"][0]["address_components"][4]["long_name"]
    location = js['results'][0]['formatted_address']
    city = js["results"][0]["address_components"][5]["long_name"]
    print('lat', lat, 'lng', lng, 'county', cou, 'address', location, 'city', city)
    cursor.execute('insert into Geodata(place,Address,Lat,Long,County,City) values (?,?,?,?,?,?)', (address,location,lat,lng,cou,city,))
    print(location)

conn.commit()
