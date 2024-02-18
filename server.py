import socket

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err))

host_ip = '127.0.0.1'
port = 1234

s.bind(('', port)) 

s.listen(5)

while True:
    c,addr = s.accept()
    print("Got connection from",addr)
    c.send("Thanks for connecting:".encode())

    c.close()
    break
































# import socket, threading

# host  = '127.0.0.1'

# port = 7976

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server.bind((host, port))
# server.listen()

# clients = []
# nicknames = []

# def broadcast(message):
#     for cleint in clients:
#         cleint.send(message)

# def handle(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             broadcast(message)
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             nickname = nicknames[index]
#             broadcast('{} left!'.format(nickname).encode('ascii'))
#             nicknames.remove(nickname)
#             break 

# def receive():
#     while True:
#         client, address = server.accept()
#         print("Connected with {}".format(str(address)))
#         client.send('NICKNAME'.encode('ascii'))
#         nickname = client.recv(1024).decode('ascii')
#         nicknames.append(nickname)
#         clients.append(client)
#         print("Nickname is {}".format(nickname))
#         broadcast("{}joined!".format(nickname).encode('ascii'))
#         client.send('Connected to server!'.encode('ascii'))
#         thread = threading.Thread(target=handle, args=(client,))
#         thread.start()

# receive()