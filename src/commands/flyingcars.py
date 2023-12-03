import ctypes
from domains import MemoryAddress
from .command import Command

class FlyingCarsCommand(Command):
    def execute(self):
        toggle = self.memory_service.read_memory(MemoryAddress(FLYINGCARS_ADDRESS), ctypes.c_byte)
        new_value = 0 if toggle == 1 else 0
        self.memory_service.write_memory(MemoryAddress(FLYINGCARS_ADDRESS), new_value, ctypes.c_byte)

