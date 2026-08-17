# Streamlit app that makes it easy to deploy a file server
import streamlit as st
import socket
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import server


class Server:

    def __init__(self, ip: str, port: int ):
        self.ip = ip
        self.port = port
        pass

    def begin_serve(self):
        # use the functions from server.py with ip and port to begin serving
        st.write("Now serving")
        return

    def end_serve(self):
        # use the functions from server.py with ip and port to begin serving, might be removed, just here for moral support
        return



def main():
    """
    server.py is the file that actually serves
    """
    if (st.button("start")):
        server = Server("0.0.0.0", 8080)
        server.begin_serve()
if __name__ == "__main__":
    main()