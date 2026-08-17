# tkinter app that makes it easy to deploy a file server
import tkinter as tk
import socket
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import server
import threading
import random


def start_server(serv: server.Server):
    serv.port = random.randrange(4000, 9999, 1)
    threading.Thread(target=serv.begin_serve).start()
    return "done"

def main():
    """
    server.py is the file that actually serves
    """
    root = tk.Tk()
    root.geometry("600x200")
    root.title("Server")
    mainframe = tk.Frame(root)
    mainframe.grid(column=0, row=0)
    serve = server.Server("0.0.0.0", 8080)
    tk.Button(
        mainframe,
        text="Serve",
        command=lambda: start_server(serve)
    ).grid(column=3, row=3)

    root.mainloop()

if __name__ == "__main__":
    main()