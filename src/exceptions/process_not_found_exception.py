class ProcessNotFoundException(Exception):
    """Exception raised when the specified process cannot be found."""
    def __init__(self, process_name: str):
        message = f"Process '{process_name}' not found"
        super().__init__(message)

