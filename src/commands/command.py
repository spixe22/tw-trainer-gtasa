from domains import GameProcess
from services import MemoryService

class Command:
    def __init__(self, game_process: GameProcess, memory_service: MemoryService):
        self.game_process = game_process
        self.memory_service = memory_service

    def execute(self, *args):
        raise NotImplementedError

    def validate(self, *args):
        pass

