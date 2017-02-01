import socket
import sys

def check_input(s):
    answer = True
    if s == '':
        answer = False
    count_space = 0
    for l in s:
        if l == ' ':
            count_space += 1
    if count_space == len(s):
        answer = False
    return answer
       

def main():
    print '=======================Let\'s chat=======================' 
    client_name = raw_input('Hello! Write your name: ')

    host = ''
    port = 30000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        s = raw_input('You: ')
        if check_input(s):
            message = client_name + ': ' + s
            sock.sendto(message, (host, port))
        result = sock.recvfrom(4064)
        print str(result[0])

if __name__ == '__main__':
    main()
