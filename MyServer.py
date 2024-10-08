# Server Program:
import socket
import threading

HEADER = 64
PORT = 5051
SERVER = "138.68.140.83"
print(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "bye"
# Hey im Teja, i have accessed the file
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}") 
        conn.send(f"Thanks from server for your message: ({msg})".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
print("PoornaSree")
print("Jayalakshmi")
print("ssteja294")
print("I am Manasa")
print("Sri Teja1")
print("tharun")
print("jayanth")
print("Naga Lakshmi G")
print("Veeresh")
print("Prem")
print("Gowtham")
start()
