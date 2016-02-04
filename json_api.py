import urllib
import json
import os.path
import datetime
import timestamp

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
print "Service:",serviceurl

while True:
    address =raw_input('Enter location: ')
    if len(address) < 1 :
        print "Invalid format. Pleaseuse text-based input"
        pass
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print "Retreiving",url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retreived',len(data),'characters'
    try:
        if len(data)<100:
            print "Invalid request! ",address,"\n",data
            continue
        else:
            js = json.loads(str(data))
            #print len(js),js
    except:
        if 'status' not in js or js['status'] != 'OK' :
            print '==== Failure to Retrieve ===='
            print js
            pass
        else:
            print "Unknown error occured",js
            continue
    while len(data)>100:
        print "\nPress (1) to read JSON\nPress (2) to get place_id\nPress (3) to get longitude and latitude data\n"
        print "Press (4) to get formatted address\nPress (5) for new location\nPress (6) to exit\n\n"
        try:
            input = int(raw_input("Function to call:"))
        except TypeError:
            print "Please use numbers to call a function. 1-2-3-4-5\n"
            pass
        if input == 1 :
            print json.dumps(js,indent = 4)
        elif input == 2:
            place_id = js["results"][0]["place_id"]
            print 'ID:',place_id
        elif input == 3:
            lat = js["results"][0]["geometry"]["location"]["lat"]
            lng = js["results"][0]["geometry"]["location"]["lng"]
            print 'lat',lat,'\nlng',lng
        elif input == 4:
            format_add = js["results"][0]["formatted_address"]
            print "Formatted address:",format_add
        elif input == 5:
            break
        elif input == 6:
            print "Ending program"
            with open(timeStamped('google_geocodeapi_log.txt'),'w') as outf:
                outf.write(data)
            q = raw_input("Press any key to confirm...")
            quit()
        else:
            print "Invalid function :",input
            pass
        with open(timeStamped('google_geocodeapi_log.txt'),'w') as outf:
            outf.write(data)
        print "Log created at log folder as:\n----google_geocodeapi_log.txt----"

