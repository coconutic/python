import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
    
    
def main():
    all_clients = set()
    host = '' 
    port = 30000
    
    server = create_socket()
    server.bind((host, port))
    while True:
        data = server.recvfrom(4064)
        cur_address = data[1][1]
        for client in all_clients:
            if cur_address != client[1]:
                server.sendto(data[0], client)
        all_clients.add(data[1])

if __name__ == '__main__':
    main()

