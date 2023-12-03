import ctypes
import psutil
from domains.game_process import GameProcess
from exceptions import ProcessNotFoundException

class ProcessService:
    @staticmethod
    def get_process_by_name(process_name: str):
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                pid = proc.pid
                handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
                return GameProcess(name=process_name, pid=pid, handle=handle)

        raise ProcessNotFoundException(process_name)

    @staticmethod
    def close_process(game_process: GameProcess):
        ctypes.windll.kernel32.CloseHandle(game_process.handle)

