import urllib
from BeautifulSoup import *
import re
import json
import ssl
import time
url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
linkc=int(raw_input("Enter count: "))
rep=int(raw_input("Enter repetitions: "))
total=(linkc*rep)
count=0
while count < total:
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    uh = urllib.urlopen(url, context=scontext)
    data = uh.read()
    print "Parsing html...\n"
    soup = BeautifulSoup(data)
    tags = soup('a')
    for tag in tags:
        link=tag.get('href', None)
        count=count+1
        if 
    print tags
    count=count+1
'''
for tag in tags :
    count=count+1
    print "Reading html...\n"
    link=tag.get('href', None)
    if count == linkc:
        if count==rep:
            print "Last page to read...",link
            print "\n",link
            break
        print "Jump to:",link
        url =link
        count = 0
        continue

    time.sleep(0.03)
    url=link


 
print "\nDone."
end=raw_input("\nPress any key to exit...")
uh.close()
'''                    
