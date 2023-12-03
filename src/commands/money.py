import ctypes
from domains import MemoryAddress
from constants import PLAYER_POINTER
from .command import Command

MONEY_ADDRESS = 0x00B7CE50 # Address for the money

class MoneyCommand(Command):
    def execute(self, *args):
        [value, ] = args
        self.memory_service.write_memory(MemoryAddress(MONEY_ADDRESS), int(value), ctypes.c_int)

