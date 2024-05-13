from socket import socket, AF_INET, SOCK_DGRAM, error
import logging
from _thread import *

logger = logging.getLogger(__name__)


class Client:
    serverIp: str
    serverPort: int
    clientAddress: tuple
    socket: socket

    def __init__(self, ip: str, port: int):
        self.serverIp = ip
        self.serverPort = port
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(('localhost', 0))
        self.clientAddress = self.socket.getsockname()

    def receiveData(self):
        while True:
            try:
                data, server_address = self.socket.recvfrom(1024)
                logger.info(f"Received from server: {data.decode()}")
            except Exception as e:
                logger.error(f"Error receiving data: {e}")
                break

    def sendData(self, data: str):
        self.socket.sendto(data.encode(), (self.serverIp, self.serverPort))


    def run(self):
        start_new_thread(self.receiveData, ())

        while True:
            data = input("Enter message to send: ")
            self.sendData(data)
            if data == "exit":
                break
        self.socket.close()
        logger.info("Client closed")
