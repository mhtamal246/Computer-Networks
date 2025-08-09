
import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
header = 64
format = 'utf-8'
disconnected_msg = "End"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg: str) -> None:
    message = msg.encode(format)
    msg_len = len(message)
    send_length = str(msg_len).encode(format)
    send_length += b' ' * (header - len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(format))

while True:
    prompt = input("Enter hours worked: ")
    if prompt == disconnected_msg:
        send(prompt)
        break
    else:
        if not prompt.isdigit():
            continue
        send(prompt)

