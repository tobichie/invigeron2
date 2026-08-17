import client_handler
import socket

def listen_accept(ip:str, port:int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1)
    client, _ = sock.accept()
    return

