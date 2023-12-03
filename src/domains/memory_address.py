class MemoryAddress:
    def __init__(self, base_address: int, offset: int = 0):
        self.base_address = base_address
        self.offset = offset

    @property
    def absolute_address(self) -> int:
        return self.base_address + self.offset

    def __str__(self):
        return f"MemoryAddress(base_address={hex(self.base_address)}, offset={hex(self.offset)}, absolute_address={hex(slef.absolute_address)})"

