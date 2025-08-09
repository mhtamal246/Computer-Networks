import socket

format= 'utf-8'
SERVER= socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
header= 64
disconnect_msg = "End"

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print("Server is starting.........")

server.listen()
print("Server is listening on", SERVER)


while True:
    conn, addr = server.accept()
    print(f"Connected to {addr}")

    connected = True
    while connected:
        msg_length = conn.recv(header).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(format)
            if msg == disconnect_msg:
                connected = False
                conn.send(f"Terminating the connection with {addr}".encode(format))
            else:
                print(f"{msg}")
                conn.send("Message received".encode(format))

    conn.close()
