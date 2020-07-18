import socket
import pickle
from tkinter import *

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!!!DISCONNECT"
GET_NEW_MESSAGES = "!!!GET_NEW_MESSAGES"
SERVER = '10.0.0.122'
ADDR = (SERVER, PORT)
FUNCTION_DELAY = 200


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
    return client.recv(2048).decode(FORMAT)

def basic_send(msg):
    message = msg.encode(FORMAT)

    client.send(message)
    return client.recv(2048).decode(FORMAT)

root = Tk()

output_frame = Frame(root, bg='#ffffff')
output_frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.7)

output_text = Text(output_frame)
output_text.place(relx=0, rely=0, relwidth=1, relheight=1)

def update_ui():
    for message in message_list:
        output_text.insert(INSERT, message)
    after(FUNCTION_DELAY, update_ui)


def get_new_messages():
    send(GET_NEW_MESSAGES)
    server_input = pickle.loads(basic_send(str(len(message_list))))
    if type(server_input) == list:
        for message in server_input:
            message_list.append(message)
    
    else:
        message_list.append(server_input)
    root.after(FUNCTION_DELAY, get_new_messages)

input_frame = Frame(root, bg='#f5f5f5')
input_frame.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)

send_message_entry = Entry(input_frame)
send_message_entry.place(relx=0, rely=0, relwidth=0.7, relheight=1)

send_message_button = Button(input_frame, bg='#49ab4e', text="Send", 
fg='#ffffff', command=lambda: send(send_message_entry.get().encode(FORMAT)))
send_message_button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

root.after(FUNCTION_DELAY, update_ui)
root.after(FUNCTION_DELAY, get_new_messages)

root.mainloop()
