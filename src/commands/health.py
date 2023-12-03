import ctypes
from domains import MemoryAddress
from constants import PLAYER_POINTER
from .command import Command

HEALTH_OFFSET = 0x540 # Offset for player health

class HealthCommand(Command):
    def execute(self, *args):
        [value, ] = args
        cPed = self.memory_service.read_memory(MemoryAddress(PLAYER_POINTER), ctypes.c_int)
        health_address = MemoryAddress(cPed, HEALTH_OFFSET)
        self.memory_service.write_memory(health_address, value, ctypes.c_float)

