from socket import socket, AF_INET, SOCK_DGRAM, error
import logging

logger = logging.getLogger(__name__)


class Server:
    ip: str
    port: int
    socket: socket

    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        # SOCK_DGRAM for udp config
        self.socket = socket(AF_INET, SOCK_DGRAM)
        try:
            self.socket.bind((str(ip), port))
        except error as e:
            logger.error(f"Error binding socket: {e}")
        logger.info(f"Server started on {ip}:{port}")
