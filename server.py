import socket
import threading

HEADER = 64
PORT = 5050
SERVER = '192.168.1.70'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!!!DICONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

message_list = []

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	
	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			message_list.append(f"[{addr}] {msg}")
			
			if msg == DISCONNECT_MESSAGE:
				connected = False
			conn.send("MSG received".encode(FORMAT))
	
	conn.close()

def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] Server is starting...")
start()
