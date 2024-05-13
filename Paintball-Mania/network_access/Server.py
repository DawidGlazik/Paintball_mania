from socket import socket, AF_INET, SOCK_DGRAM, error
from network_access.GameManager import GameManager
import random
import logging

logger = logging.getLogger(__name__)


class Server:
    ip: str
    port: int
    socket: socket
    gameManagers: list[GameManager]

    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        # SOCK_DGRAM for udp config
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.gameManagers = []
        try:
            self.socket.bind((str(ip), port))
        except error as e:
            logger.error(f"Error binding socket: {e}")
        logger.info(f"Server started on {ip}:{port}")

    def hostNewGame(self, clientAddress):
        gameCode: int = random.randint(1,1000)
        while gameCode in [game.gameCode for game in self.gameManagers]:
            gameCode = random.randint(1, 1000)

        newGameManager: GameManager = GameManager(gameCode, clientAddress)
        newGameManager.clients.append(clientAddress)

        self.gameManagers.append(newGameManager)
        newGameManager.initializeGame()

        logger.info(f"New game hosted by {clientAddress} - GAME ID: {gameCode}")

    def sendData(self, data: str, clientAddress):
        self.socket.sendto(data.encode(), clientAddress)

    def connectPlayerToGame(self, clientAddress, decodedMessage: str):
        for game in self.gameManagers:
            if decodedMessage == str(game.gameCode):
                logger.info(f"Game {game.gameCode} joined by {clientAddress}")
                game.clients.append(clientAddress)
                break


    def run(self):
        while True:
            try:
                message, clientAddress = self.socket.recvfrom(1024) # 1024 rozmiar bufora
                decodedMessage: str = message.decode()
                logger.debug(f"Received message from {clientAddress}: {decodedMessage}")
                # handle player joining the game
                if decodedMessage.isnumeric():
                    self.connectPlayerToGame(clientAddress, decodedMessage)
                # handle player hosting the game
                if decodedMessage == "host":
                    self.hostNewGame(clientAddress)
            except error as e:
                logger.error(f"Error receiving message: {e}")
        self.socket.close()

