import socket


class Server:

    def __init__(self, ip: str, port: int ):
        self.sock = None
        self.ip = ip
        self.port = port

    def begin_serve(self):
        # use the functions from server.py with ip and port to begin serving        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("begin serve on socket:", self.sock)
        print("Port:", self.port)
        sock, client = self.listen_accept(self.sock)
        print("accepted client:", client)
        return


    def listen_accept(self, sock: socket.socket):
        sock.bind((self.ip, self.port))
        sock.listen(1)
        client, _ = sock.accept()
        return sock, client