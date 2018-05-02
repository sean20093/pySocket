import socket
import sys

# Send Reference: https://pymotw.com/2/socket/udp.html


def connect_to_server(address, port, command):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (address, port)

    try:
        # Send data
        print >>sys.stderr, 'sending "%s"' % command
        sent = sock.sendto(command, server_address)

        # Receive response
        print >>sys.stderr, 'waiting to receive'
        data, server = sock.recvfrom(4096)
        print >>sys.stderr, 'received "%s"' % data

        if data != 'Could not fetch file. ':
            fd = open('syslog', 'w')
            fd.write(data)
            fd.close()
        else:
            print >> sys.stderr, data

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()


def get_user_input():

    name = raw_input("\nEnter server name or IP address:")
    try:
        address = socket.gethostbyname(name)
        print 'Entered address is %s' % address
    except socket.gaierror:
        print("\nCould not connect to server. ")
        exit(1)

    port = int(raw_input("\nEnter port:"))
    if port < 0 or port > 65535:
        print "Invalid port number"
        exit(1)

    command = raw_input("\nEnter command:")

    return address, port, command

address, port, command = get_user_input()
connect_to_server(address, port, command)


