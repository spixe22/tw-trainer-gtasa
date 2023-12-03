class GameProcess:
    def __init__(self, name: str, pid: int, handle: int):
        self.name = name
        self.pid = pid
        self.handle = handle

    def __str__(self):
        return f"GameProcess(name={self.name}, pid={self.pid}, handle={self.handle})"

    def is_active(self) -> bool:
        # Implement logic to check if the process is still active
        pass

