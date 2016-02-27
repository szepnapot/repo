import urllib
import json

class Geocode():
    "Google's Geocode API wrapper"

    def __init__(self,location = '',geoinfo ={}):
        "basic parematers for json request, location and api key"
        self.loc = location
        self.service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
        self.geoi = geoinfo
    def loc_search(self,search):
        "user search for a location(string)"
        if len(search) < 2:
            print "Invalid input, search string must be longer than 2 characters."
            print search+"is"+len(search)+"charachters"
        self.search = str(search)
        self.loc = self.search
        search_url = self.service_url + urllib.urlencode({'sensor':'false', 'address': self.loc,'language': 'hu'})
        uh = urllib.urlopen(search_url)
        raw_data = uh.read()
        self.data = raw_data
        return self.data
        return self.loc

    def json_req(self):
        "json request with error handling"
        try:
            js = json.loads(str(self.data))
            self.js = js
        except:
            print "Unknown error occured",self.data
            quit()
        if js['status'] != 'OK' :
            print '==== Failure to Retrieve ===='
            print "Sorry, we haven't found a route for your request :("
            #print js
            pass
        return self.js

    def geodata(self):
        "basic geodata, placeid, full address, lat/lng"
        place_id = self.js["results"][0]["place_id"]
        formatadd = self.js["results"][0]["formatted_address"]
        self.lat = self.js["results"][0]["geometry"]["location"]["lat"]
        self.lng = self.js["results"][0]["geometry"]["location"]["lng"]
        gps_loc = (self.lat,self.lng)
        self.geoi['gps'] = gps_loc
        self.geoi['address'] = formatadd
        self.geoi['id'] = place_id
        return self.geoi

