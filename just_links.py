#links from given url
#if lst 1, make a list of links
#if 0 no list
def links(url):
    
    #import libs
    import urllib
    import socket
    import sys
    from BeautifulSoup import *

    #open url and parse with BeautifulSoup
    data = urllib.urlopen(url)
    html = data.read()
    soup = BeautifulSoup(html)
    #list for links
    linkek = []
    #get anchors
    tags = soup('a')
    #loop for links
    for link in tags:
        link_url = link.get('href')
        print link_url
        #put links into 'linkek' list
        linkek.append(link_url)
    data.close()

    
