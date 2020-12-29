import socket

HOST = "192.168.YOUR IP"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen()

client, address = server.accept()

while True:
    print(f"Connected to {address}")

    cmd_input = input("Enter a command: ")
    client.send(cmd_input.encode('utf-8'))

    print(client.recv(1024).decode('utf-8'))

    
    

