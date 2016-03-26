import urllib
import socket
import re
import json
import ssl
import time
import xml.etree.ElementTree as ET

url= 'http://python-data.dr-chuck.net/comments_42.html'
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
data = uh.read()

while True:
    print 'Retrieving', url
 
    print 'Retrieved',len(data)
    tree = ET.fromstring(data)

    counts = tree.findall('comment/count')
    print 'COUNTS:',len(counts)



