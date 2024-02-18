import socket

s = socket.socket()

host_ip = '127.0.0.1'
port = 1234

s.connect((host_ip,port))

print(s.recv(1024).decode())

s.close()
























# import socket, threading

# host = '127.0.0.1'

# port = 9001

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((host, port))
# server.listen()

# clients = []
# nicknames = []
# rooms = []

# def broadcast(message, c):
#     for client in clients:
#         if client!=c:
#             client.send(message.encode('ascii'))

# def handle_rooms(roomId, cleints,)

# def handle(client):
#     while True:
#         try:
#             message = client.recv(1024).decode('ascii')
#             broadcast(message, client)
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             nickname = nicknames[index]
#             broadcast('{} left!'.format(nickname).encode('ascii'), client)
#             nicknames.remove(nickname)
#             break 


# def receive():
#     while True:
#         client, addr = server.accept()
#         print("Connect with {}".format(str(addr)))
#         nickname = client.recv(1024).decode('ascii')
#         nicknames.append(nickname)
#         clients.append(client)
#         print("Nickname is {}".format(nickname))
#         broadcast("{} joined the room".format(nickname), client)
#         # client.send("Connected tothe server".encode('ascii'))
#         thread = threading.Thread(target=handle, args=(client,))
#         thread.start()
# receive()