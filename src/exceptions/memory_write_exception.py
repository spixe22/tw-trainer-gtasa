class MemoryWriteException(Exception):
    """Exception raised for errors in the memory write operation."""
    def __init__(self, address: int):
        message = f"Failed to write memory at address: {hex(address)}"
        super().__init__(message)

