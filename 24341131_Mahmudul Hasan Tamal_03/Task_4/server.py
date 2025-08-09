
import socket

format = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
header = 64
disconnected_msg = "End"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

            if msg == disconnected_msg:
                connected = False
                conn.send(f"Terminating the connection with {addr}".encode(format))
            else:
                hours = int(msg)
                if hours <= 40:
                    salary = hours * 200
                else:
                    salary = 8000 + (hours - 40) * 300

                response = f"Calculated salary: Tk {salary}"
                conn.send(response.encode(format))

    conn.close()
