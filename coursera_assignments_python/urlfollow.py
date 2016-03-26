# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import re
import json
import ssl
import time

linkc=int(raw_input("Enter count: "))
rep=int(raw_input("Enter repetitions: "))

url =  'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
print 'Retreiving',url
confirm=raw_input("Press any key to continue...")
time.sleep(0.125)

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
data = uh.read()
soup = BeautifulSoup(data)

# Retrieve all of the anchor tags
count=0
repe=0
tags = soup('a')
#print type(tags)

for tag in tags :
        print "Reading html...\n"
        link=tag.get('href', None)
        count=count+1
        print count,"\n"
        
        if count==linkc:
                repe=repe+1
                url=link
                                        
                print "Link",linkc,"in repetition",repe,"\n",url
                uh = urllib.urlopen(url, context=scontext)
                data = uh.read()
                soup = BeautifulSoup(data)
                print "Jumping to the next page..."
                time.sleep(0.05)
                
                tags=soup('a')
                count=0
                print "Current page count reset..."
                continue
        if repe==rep:
                uh = urllib.urlopen(url, context=scontext)
                data = uh.read()
                soup = BeautifulSoup(data)
                tags=soup('a')
                time.sleep(0.05)
                print "Current count:",count,"\n"
                if count == linkc:
                        print "Last link is:\n",link
                        break

print "\nDone."
end=raw_input("\nPress any key to exit...")
uh.close()
             
                
