class MemoryReadException(Exception):
    """Exception raised for errors in the memory read operation."""
    def __init__(self, address: int):
        message = f"Failed to read memory at address: {hex(address)}"
        super().__init__(message)

