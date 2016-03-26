import urllib
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 or acct == 'end') : break
    while True:
        try:
            cout = int(raw_input('Enter tweet count:'))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."            
    url = twurl.augment(TWITTER_URL,
        {'screen_name': acct, 'count': cout} )
    print 'Retrieving', url
    connection = urllib.urlopen(url)
    data = connection.read()
    headers = connection.info().dict
    print '\nRemaining', headers['x-rate-limit-remaining']
    js = json.loads(data)
    #print json.dumps(js, indent=4)

    for u in js['users'] :
        print u['screen_name']
        s = u['status']['text']
        print '  ',s[:]
