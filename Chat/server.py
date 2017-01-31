import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
    
    
def main():
    server = create_socket()
    host = '' 
    port = 30000
    server.bind((host, port))
    while True:
        all_clients = []
        server.listen(2)
        db = []
        for i in xrange(2):
            new_connection, address = server.accept()
            all_clients.append(new_connection)
            data = new_connection.recv(4096)
            if not data:
                continue
            db.append(data)
        for i in db:
            all_clients[0].sendall(i)
            all_clients[1].sendall(i)
        for i in all_clients:
            i.close()


if __name__ == '__main__':
    main()

