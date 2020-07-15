import socket
from tkinter import *

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!!!DISCONNECT"
GET_NEW_MESSAGES = "!!!GET_NEW_MESSAGES"
SERVER = '192.168.1.70'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


message_list = []

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))
	
def get_new_messages():
	

root = Tk()
output_frame = Frame(root, bg='#ffffff')
output_frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.7)

output_text = Text(output_frame)
output_text.place(relx=0, rely=0, relwidth=1, relheight=1)

input_frame = Frame(root, bg='#f5f5f5')
input_frame.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)

send_message_entry = Entry(input_frame)
send_message_entry.place(relx=0, rely=0, relwidth=0.7, relheight=1)

send_message_button = Button(input_frame, bg='#49ab4e', text="Send", 
fg='#ffffff', command=lambda: send(send_message_entry.get()))
send_message_button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

root.mainloop()
