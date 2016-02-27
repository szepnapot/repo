# -*- coding: utf-8 -*-
'''
Created by: Peter Lodri
just for fun, at to learn by creating something

2016.02.26

'''
from direction import *
from geocode import *
from wiki import *

g = Geocode()
d = Direction()
w = WikiInfo()

def wiki_call(search,lang):
    #title, url in a tuple ---> self.i['search']
    w.search_info(search)
    info = w.page_info()
    pageh = wikipedia.summary(search)
    print pageh

def geo_id(search):
    g.loc_search(search)
    g.json_req()
    geo_info = g.geodata()
    geo_idp = geo_info['id']
    print geo_idp

def geo_call(search):
    g.loc_search(search)
    g.json_req()
    geo_info = g.geodata()
    print "////////////////////////////////////////////////"
    print "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
    print "Full name of request:",geo_info['address']
    print "Latitude, longitude:",geo_info['gps']
    print "Place ID:",geo_info['id']
    print "////////////////////////////////////////////////"
    print "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
    
def direct_call(s,e,m):
    d.travel_params(start=s,end=e,mode=m)
    d.connect()
    d.json_data()
    trav_inf = d.info()
    print "////////////////////////////////////////////////"
    print "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
    print "Start:",trav_inf['start address']
    print "     Lat,lng:",trav_inf['start lat'],trav_inf['start lng']
    print "End:",trav_inf['end address']
    print "     Lat,lng:",trav_inf['end loc lat'],trav_inf['end loc lng']
    print "Mode of travel:",trav_inf['mode'].lower()
    print "------------------------------------------------"
    print "Distance:",trav_inf['distance']
    print "Duration of the travel:",trav_inf['duration']
    print "////////////////////////////////////////////////"
    print "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"


print """This little program goal is to help hitchikers around the world if they stuck \
\nor just want some useful information about their next destination. \
\nYou can either get some helpful geo-info about given locations, like gps coordinates \
\nfull formatted address, or geolocical ID for further use. \
\nA route planner also included with basic information about the travel, \
\nlike duration of the travel or distance. Cycling and walking are not fully supported, \
\nshort distances are ok, but for very long bike trips ( more than 100-200 km ) \
\nI don't recommend it :)
\nA Wikipedia wrapper also helps you to get more knowledge about your next town. \
\nYou can also save it for offline use! :) \
\nFeel free to email me with suggestions, report bugs etc. at: \
\nsilentpocok @ gmail . com\n\n"""



while True:
    search = str(raw_input("\nEnter location: "))
    geo_call(search)
    e = raw_input("Enter end location: ")
    geo_call(e)
    print "Three travel mode available, 'driving', 'walking' or 'bicycling'"
    m = raw_input("Please type in travel mode: ")
    s = search
    direct_call(s,e,m)
    routemap = raw_input("If you want to view your route via Google Maps type '+omap': ")
    if routemap == "+omap":
        print "\nCopy-paste these ID-s into the map.html file located in the folder."
        print "\nStart ID:",geo_id(search)
        print "End ID:",geo_id(e)

    ews = str(raw_input("\nWant a short Wiki summary of the end location? (Y)es or (N)o :"))
    if ews == 'y':
        wikilang = str(raw_input("Set text language (eg.: 'hu', 'en', 'fr'):"))
        w.lang_select(wikilang)
        wiki_call(e,wikilang)
        call = True
    elif ews == 'n':
        call = False
        pass

    if call == True:
        wikifile = raw_input("\nWant to save the complete Wiki page for offline use? (Y)es or (N)o :")
        if wikifile == 'y':
            w.search_info(e)
            w.page_info()
            w.txt_write()
        elif wikifile == 'n':
            pass

    elif call == False:
        print "Type quit for exit the program \nor press any key to continue with a new request."
        ask = raw_input("\n Type '-quit' or press any key: ")
        if ask == '-quit':
            break
            quit()
        else:
            pass


    

    
    
