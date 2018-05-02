import socket
import sys
import os

# Bind Reference: https://pymotw.com/2/socket/udp.html

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    print >> sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)

    print >> sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >> sys.stderr, data

    if data:
        val = os.system(data)
        content = os.popen(data).read()

        if val == 0:
            sent = sock.sendto(content, address)
            print >> sys.stderr, 'sent %s bytes back to %s' % (sent, address)
        else:
            sent = sock.sendto('Could not fetch file. ', address)

