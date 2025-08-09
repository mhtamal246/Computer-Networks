import socket
import threading

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


def handle_clients(conn, addr):
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
                vowels = "aeiouAEIOU"
                count = 0
                for char in msg:
                    if char in vowels:
                        count += 1
                if count == 0:
                    response = "Not enough vowels"
                elif count <= 2:
                    response = "Enough vowels I guess"
                else:
                    response = "Too many vowels"

                conn.send(response.encode(format))

    conn.close()


while True:
    conn, addr = server.accept()
    thread= threading.Thread(target=handle_clients, args=(conn, addr))
    thread.start()
    