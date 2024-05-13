from game_logic.Board import Board
from network_access.Client import Client
from enum import Enum
import logging
from _thread import *
import os
import time

logger = logging.getLogger(__name__)


class GameState(Enum):
    FINISHED = 1
    RUNNING = 2
    WAITING = 3


class GameManager:
    gameHost: str
    clients: list
    board: Board
    gameStatus: GameState
    playersData: list[str]
    gameCode: int

    def __init__(self, gameCode: int, host: str):
        self.gameHost = host
        self.gameCode = gameCode
        self.clients = []
        self.board = None
        self.gameStatus = GameState.WAITING
        self.playersData = []

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def gameHandling(self):
        while self.gameStatus == GameState.WAITING:
            print(f"Waiting for players to join... - Game hosted by {self.gameHost} - ID: {self.gameCode}")
            print(f"Players joined: {len(self.clients)}")
            for address in self.clients:
                print(address)
            time.sleep(3)
            os.system('cls')

            game_info = f"Game hosted by {self.gameHost}, ID: {self.gameCode}"

    def initializeGame(self):
        self.board = Board(10)
        logger.info(f"Game {self.gameCode} initialized")
        start_new_thread(self.gameHandling, ())


