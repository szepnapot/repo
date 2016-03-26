import urllib
from twurl import augment
import json

print "reads a Twitter account's timeline"

while True:
        try:
            cout = int(raw_input('Enter tweet count:'))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."     

print '* Calling Twitter...'
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': 'Theidden_one', 'count': cout} )
print url[:100]
connection = urllib.urlopen(url)
data = connection.read()
#print data
headers = connection.info().dict
#print headers
print '\nRemaining', headers['x-rate-limit-remaining']
js = json.loads(data)
#print json.dumps(js, indent=4)

for u in js:
    print u['text']
