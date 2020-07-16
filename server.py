import socket
import threading

HEADER = 64
PORT = 5050
SERVER = '192.168.1.5'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!!!DICONNECT"
GET_NEW_MESSAGES = "!!!GET_NEW_MESSAGES"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

message_list = []

def send_new_messages(conn, messages_read):
	count = 0
    for message in len(message_list):
        if count < messages_read and count <= len(message_list):
        	pass # For now

        elif count <:
        	count += 1
    


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
            
            if msg  == GET_NEW_MESSAGES:
                messages_read = int(conn.recv(HEADER).decode(FORMAT))
                
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
