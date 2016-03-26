import socket

inpurl=raw_input('Enter url--')
url1=inpurl.split('/')
url2=str(url1[2])
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url2, 80))
mysock.send('GET inpurl HTTP/1.1\n')
mysock.send('Host: url2\n\n' )

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()
