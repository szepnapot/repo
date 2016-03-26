'''
Summarize the value of a variable in the given xml tree
using json,urllib,xml.etree,ssl
'''
import urllib
import xml.etree.ElementTree as ET
import json
import ssl
#open url with SSL
url = 'http://python-data.dr-chuck.net/comments_202059.xml'
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
#read url, string
data = uh.read()
#xml tree object
tree = ET.fromstring(data)
#find "comments" node
comm = tree.find('comments')
#creat a list the found numbers
szamok = []
#from comments node find all "comment" element and 
#i want the "count" called from that and just the text
#formatted value of it, and we convert it for int 
for counts in comm.findall('comment'):
    counts = int(counts.find('count').text)
    szamok.append(counts)
#int for proper call of sum() function is needed
total = sum(szamok)
print total



