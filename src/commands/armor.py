import ctypes
from domains import MemoryAddress
from constants import PLAYER_POINTER
from .command import Command

ARMOR_OFFSET = 0x548 # Offset for player armor

class ArmorCommand(Command):
    def exectute(self, *args):
        [value, ] = args
        cPed = self.memory_service.read_memory(MemoryService(PLAYER_POINTER), ctypes.c_int)
        armor_address = MemoryService(cPed, ARMOR_OFFSET)
        self.memory_service.write_memory(armor_address, value, ctypes.c_float)

