from socket import socket, AF_INET, SOCK_DGRAM, error
import logging

logger = logging.getLogger(__name__)


class Client:
    ip: str
    port: int

    def __init__(self, ip: str, port: int):
        pass