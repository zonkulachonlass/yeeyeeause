from __future__ import print_function	# For Py2/3 compatibility
import math
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from geopy.geocoders import Nominatim
from math import radians, cos, sin, asin, sqrt
UP = '\033[1A'
CLEAR = '\x1b[2K'
import eel
from random import randint
  
eel.init('wesiteStudd')
  
"""# Exposing the random_python function to javascript
@eel.expose    
def random_python(x):
    x=x
    return x"""

@eel.expose
def random_python(excludeNonFreq, measuringSystem, userCoordsLa, userCoordsLo):
    #excludeNonFreq=True
    #measuringSystem='Imperial'
    #userCoordsLa='38.743339'
    #userCoordsLo='-121.265084'
    if excludeNonFreq == 'Yes':
        excludeNonFreq = True
    elif excludeNonFreq == 'No':
        excludeNonFreq = False


    def loadingBar(percent, length):
        percent = float(percent)
        length = float(length)
        numOfSpaces = int(str(percent/(100/length)).split('.')[0])
        numofnoSpaces = length - numOfSpaces
        x = 0
        shadedSpaces = []
        nonShadedSpaces = []
        while x != numOfSpaces:
            x = x + 1
            shadedSpaces.append(' ')
            
        x = 0
        while x != numofnoSpaces:
            x = x + 1
            nonShadedSpaces.append(' ')
            
        shadedSpaces = ''.join(shadedSpaces)
        nonShadedSpaces = ''.join(nonShadedSpaces)
        progressBar = '|' + '\x1b[0;31;41m' + shadedSpaces + '\x1b[0m'+ nonShadedSpaces +'|' + str(percent) + '%'
        return progressBar
    def coordsToAddress(lat, lon):
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.reverse("{0}, {1}".format(lat, lon))
        address = location.raw['address']
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
        zipcode = address.get('postcode')
        if country == 'United States':
            country = "USA"
        array = [country, state, zipcode, city]
        return array
    def distance_between(latA, lonA, latB, lonB):
        y = abs(latA-latB) ** 2
        x = abs(lonA-lonB) ** 2
        return math.sqrt(x + y)
    def distance(lat1, lat2, lon1, lon2):
        lon1 = radians(float(lon1))
        lon2 = radians(float(lon2))
        lat1 = radians(float(lat1))
        lat2 = radians(float(lat2))
        

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    
        c = 2 * asin(sqrt(a))
        r = 6371
        
        return(c * r)
    def degree_cleanup(measurment):
        asdf = []
        degrees = []
        minuits = []
        seconds = []
        x=0
        while True:
            try:
                asdf.append(measurment[x])
            except:
                break
            x = x + 1
        letter = asdf[0]
        x = 2
        while True:
            if asdf[x] == ' ':
                break
                
            else:
                degrees.append(asdf[x])
            x = x + 1
        
        minuits.append(asdf[x + 1])
        minuits.append(asdf[x + 2])
        seconds.append(asdf[x + 5])
        seconds.append(asdf[x + 6])
        deg = ''.join(degrees)
        min = ''.join(minuits)
        sec = ''.join(seconds)
        min = int(min) * 0.01666666666
        sec = int(sec) * 0.000277777778
        output = int(deg) + min + sec
        if letter == 'S' or letter == 'W':
            output = -output
        return output
    def dCoords(cleanedcoord, LAToLON):
        #has to be cleaned
        if LAToLON.lower() == 'lon':
            dCoord = float(cleanedcoord) + 180
        elif LAToLON.lower() == 'lat':
            dCoord = float(cleanedcoord) + 90
        return dCoord
    def percent(a, b):
        c = a/b
        c = c * 100
        c = int(c)
        return(c)
    def city_to_coords(city, state, country):
        try:
            geolocator = Nominatim(user_agent="Your_Name")
            location = geolocator.geocode(city+','+state+','+ country)
            coords = [location.latitude, location.longitude, False]
        except:
            coords = ['', '', True]
        return coords
    #if city_to_coords(values)[2] == False:
    
    while True:
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(executable_path='<path-to-chrome>', options=options)
            driver.get('https://www.yaesu.com/jp/en/wires-x/id/active_node.php')
        except:
            output = 'Internet Connection Error'
            break
        if excludeNonFreq == 'Yes':
            excludeNonFreq = True
        elif excludeNonFreq == 'No':
            excludeNonFreq = False
        else:
            output = 'Input Error'
        try:
            DuserCoordsLat = dCoords(userCoordsLa, 'lat')
            DuserCoordsLon = dCoords(userCoordsLo, 'lon')
            addy = coordsToAddress(userCoordsLa, userCoordsLo)
        except:
            output = 'ValueError: Must be a coordinate pair or Point'
            break
        if measuringSystem == 'Imperial':
            levalue = 1.609
            lelevalue = 'miles'
        elif measuringSystem == 'Metric':
            levalue = 1
            lelevalue = 'kilometers'
        else:
            output = 'Measuring System Error'
            break
        ui1 = addy[0]
        ui2 = addy[1]
        ui3 = addy[3]

        print(ui1, ui2, ui3)
        #if city_to_coords(ui3, ui2, ui1)[2] != True:

        content = driver.page_source
        soup = BeautifulSoup(content, 'lxml')
        loi = soup.find_all('tr')
        x = 1
        NODEID = []
        DTMFID = []
        ANA_DIG = []
        CALLSIGN = []
        CITY = []
        STATE = []
        COUNTRY = []
        FREQ = []
        SQL = []
        LAT = []
        LON = []
        LATD = []
        LOND = []
        COMMENT = []
        EXACT_COORDS = []
        COORD_FAILED = []
        print()
        print()

        while x != len(loi):
            tag = loi[x].find_all('td')
            freq = tag[7].text
            lon = tag[10].text
            lony = []
            y = 0
            while True:
                try:
                    lony.append(lon[y])
                except:
                    break
                y = y + 1
            try:
                lony.pop(-1)
            except:
                lony = lony
            lon = ''.join(lony)
                
            if tag[6].text == ui1:
                if tag[5].text == ui2:
                    if excludeNonFreq == True:
                        if freq != '':
                            if lon == '' or lon == "E:001 01' 01" or lon == "E:000 00' 00" or lon == ' ':
                                city_to_coords_output = city_to_coords(tag[4].text, tag[5].text, tag[6].text)
                                if city_to_coords_output[2] == True:
                                    x = x + 1
                                    continue
                                
                                NODEID.append(tag[0].text)
                                DTMFID.append(tag[1].text)
                                CALLSIGN.append(tag[2].text)
                                ANA_DIG.append(tag[3].text)
                                CITY.append(tag[4].text)
                                STATE.append(tag[5].text)
                                COUNTRY.append(tag[6].text)
                                FREQ.append(tag[7].text)
                                SQL.append(tag[8].text)
                                LAT.append(city_to_coords_output[0])
                                LON.append(city_to_coords_output[1])
                                COMMENT.append(tag[11].text)
                                EXACT_COORDS.append(False)
                                COORD_FAILED.append(city_to_coords_output[2])
                                LATD.append(dCoords(city_to_coords_output[0], 'lat'))
                                LOND.append(dCoords(city_to_coords_output[1], 'lon'))
                            else:
                                NODEID.append(tag[0].text)
                                DTMFID.append(tag[1].text)
                                CALLSIGN.append(tag[2].text)
                                ANA_DIG.append(tag[3].text)
                                CITY.append(tag[4].text)
                                STATE.append(tag[5].text)
                                COUNTRY.append(tag[6].text)
                                FREQ.append(tag[7].text)
                                SQL.append(tag[8].text)
                                LAT.append(degree_cleanup(tag[9].text))
                                LON.append(degree_cleanup(lon))
                                COMMENT.append(tag[11].text)
                                EXACT_COORDS.append(True)
                                COORD_FAILED.append(False)
                                LATD.append(dCoords(degree_cleanup(tag[9].text), 'lat'))
                                LOND.append(dCoords(degree_cleanup(lon), 'lon'))
                    else:
                        if lon == '' or lon == "E:001 01' 01" or lon == "E:000 00' 00" or lon == ' ':
                            city_to_coords_output = city_to_coords(tag[4].text, tag[5].text, tag[6].text)
                            if city_to_coords_output[2] == True:
                                x = x + 1
                                continue
                            NODEID.append(tag[0].text)
                            DTMFID.append(tag[1].text)
                            CALLSIGN.append(tag[2].text)
                            ANA_DIG.append(tag[3].text)
                            CITY.append(tag[4].text)
                            STATE.append(tag[5].text)
                            COUNTRY.append(tag[6].text)
                            FREQ.append(tag[7].text)
                            SQL.append(tag[8].text)
                            LAT.append(city_to_coords_output[0])
                            LON.append(city_to_coords_output[1])
                            COMMENT.append(tag[11].text)
                            EXACT_COORDS.append(False)
                            COORD_FAILED.append(city_to_coords_output[2])
                            LATD.append(dCoords(city_to_coords_output[0], 'lat'))
                            LOND.append(dCoords(city_to_coords_output[1], 'lon'))
                        else:
                            NODEID.append(tag[0].text)
                            DTMFID.append(tag[1].text)
                            CALLSIGN.append(tag[2].text)
                            ANA_DIG.append(tag[3].text)
                            CITY.append(tag[4].text)
                            STATE.append(tag[5].text)
                            COUNTRY.append(tag[6].text)
                            FREQ.append(tag[7].text)
                            SQL.append(tag[8].text)
                            LAT.append(degree_cleanup(tag[9].text))
                            LON.append(degree_cleanup(lon))
                            COMMENT.append(tag[11].text)
                            EXACT_COORDS.append(True)
                            COORD_FAILED.append(False)
                            LATD.append(dCoords(degree_cleanup(tag[9].text), 'lat'))
                            LOND.append(dCoords(degree_cleanup(lon), 'lon'))
            print(UP, end=CLEAR)
            x = x + 1   
            print('Scanning Repeater Id {0} Progress: {1}'.format(tag[0].text, loadingBar(percent(x, len(loi)), 40)))
            
        bestOption = 0
        lowest = distance_between(DuserCoordsLat, DuserCoordsLon, LATD[0], LOND[0])
        x = 1
        while x != len(LATD):
            if distance_between(DuserCoordsLat, DuserCoordsLon, LATD[x], LOND[x]) < lowest:
                lowest = distance_between(DuserCoordsLat, DuserCoordsLon, LATD[x], LOND[x])
                bestOption = x
            elif distance_between(DuserCoordsLat, DuserCoordsLon, LATD[x], LOND[x]) == lowest:
                lowest = distance_between(DuserCoordsLat, DuserCoordsLon, LATD[x], LOND[x])
                bestOption = x
            x = x + 1

        intro = 'Out of all the Wires X repeaters I found that the closest one happens to be {0} around {1} {2} away. The following contains information about this repeater:'.format(CALLSIGN[bestOption], distance(LAT[bestOption], userCoordsLa, LON[bestOption], userCoordsLo)*levalue, lelevalue)
        info = 'Call Sign: {0}'.format(CALLSIGN[bestOption])
        info2 = 'Location: {0}, {1}, {2} at coordinates lat: {3} lon: {4} '.format(CITY[bestOption], STATE[bestOption], COUNTRY[bestOption], LAT[bestOption], LON[bestOption])
        info3 = 'Freq(MHz): {0} SQL: {1} Analog/Digital: {2}'.format(FREQ[bestOption], SQL[bestOption], ANA_DIG[bestOption])
        info4 = 'If False exact coordinates of repeater are unknown(less acurate): {0}'.format(EXACT_COORDS[bestOption])
        info5 = 'NODE ID: {0}'.format(NODEID[bestOption])
        info6 = 'DTMF ID: {0}'.format(DTMFID[bestOption])
        info7 = 'Comment: {0}'.format(COMMENT[bestOption])
        info8 = 'Potential Error: {0}'.format(COORD_FAILED[bestOption])

        output = [intro, info, info2, info3, info4, info5, info6, info7, info8]
        break
    print()
    print(output)
    print('closing program....')
    return output

# Start the index.html file
eel.start('index.html')    # Start

