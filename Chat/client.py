import socket
import sys

host = ''
port = 30000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    s = raw_input()
    if s != '':
        sock.sendto(s, (host, port))
    result = sock.recvfrom(4064)
    print str(result[0])

