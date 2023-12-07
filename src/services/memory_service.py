import ctypes
from domains.memory_address import MemoryAddress
from domains.game_process import GameProcess

class MemoryService:
    def __init__(self, game_process: GameProcess):
        self.game_process = game_process

    def read_memory(self, memory_address: MemoryAddress, data_type=ctypes.c_int) -> int:
        buffer = data_type()
        ctypes.windll.kernel32.ReadProcessMemory(self.game_process.handle, memory_address.absolute_address, ctypes.byref(buffer), ctypes.sizeof(buffer), None)
        return buffer.value

    def write_memory(self, memory_address: MemoryAddress, value: int, data_type=ctypes.c_int):
        buffer = data_type(value)
        ctypes.windll.kernel32.WriteProcessMemory(self.game_process.handle, memory_address.absolute_address, ctypes.byref(buffer), ctypes.sizeof(buffer), None)

