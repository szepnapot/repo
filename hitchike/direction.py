import urllib
import json

class Direction():
    "Google Directions API wrapper"

    def __init__(self,api_key = None,travelinfo={}):
        if api_key is None:
            api_key = 'AIzaSyADAh9sV270lUkQoMiEtCmlRrrzy02FTUo'
            self.key = api_key
        service_url = 'https://maps.googleapis.com/maps/api/directions/json?'
        self.service_url = service_url
        self.ti = travelinfo

    def travel_params(self,start='',end='',mode='driving',region = 'hu'):
        "connect to Directions api and send request with the following requests:"
        "start loc, end loc, travel mode (default is driving, can be bicycling or walking)"
        if len(start) < 2 or len(end) <2:
            print "Start and end location can't be empty"
            start_loc = str(raw_input("Enter start location:"))
            end_loc = str(raw_input("Enter end location:"))
            self.start = start_loc
            self.end = end_loc
            pass
        self.start = start
        self.end = end
        self.mode = mode
        self.region = region
        return self.start
        return self.end
        return self.mode
        return self.region

    def connect(self):
        url = self.service_url + urllib.urlencode({'origin': self.start,'destination': self.end,'key':self.key,'mode':self.mode,'region':self.region})
        uh = urllib.urlopen(url)
        data = uh.read()
        if len(data)<50:
            print "Invalid request!"
            print data
        self.data =data
        return self.data

    def json_data(self):
        "json request"
        try:
            js = json.loads(str(self.data))
            self.js = js
        except:
            print "Unknown error occured",self.data
            quit()
        if js['status'] != 'OK' :
            print '==== Failure to Retrieve ===='
            #print js
            print "\n Sorry, we haven't found a route."
            quit()
        return self.js

    def info(self):
        "information about the route, travel mode, start+end lat/lng, duration"
        "distance, start+end address, put into a dictionary"
        travel_mode = self.js["routes"][0]["legs"][0]["steps"][0]["travel_mode"]
        start_loc_lat = self.js["routes"][0]["legs"][0]["steps"][0]["start_location"]["lat"]
        start_loc_lng = self.js["routes"][0]["legs"][0]["steps"][0]["start_location"]["lng"]
        end_loc_lat = self.js["routes"][0]["legs"][0]["steps"][0]["end_location"]["lat"]
        end_loc_lng = self.js["routes"][0]["legs"][0]["steps"][0]["end_location"]["lng"]
        duration = self.js["routes"][0]["legs"][0]["duration"]["text"]
        distance = self.js["routes"][0]["legs"][0]["distance"]["text"]
        start_add = self.js["routes"][0]["legs"][0]["start_address"].encode('utf-8')
        end_add = self.js["routes"][0]["legs"][0]["end_address"].encode('utf-8')
        self.ti['mode'] = travel_mode
        self.ti['start lat'] = start_loc_lat
        self.ti['start lng'] = start_loc_lng
        self.ti['end loc lat'] = end_loc_lat
        self.ti['end loc lng'] = end_loc_lng
        self.ti['duration'] = duration
        self.ti['distance'] = distance
        self.ti['start address'] = start_add
        self.ti['end address'] = end_add
        return self.ti


