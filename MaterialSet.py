from aset import *

class MaterialSet(ASet):
    """
    Set ADT for storing the trader's materials
    """

    def init(self, capacity: int = 1) -> None:
        super().__init__()
        self.array = ArrayR(max(1, capacity))


    def clear(self) -> None:
        self.size = 0

    def len(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return len(self) == 0

    def is_full(self) -> bool:
        return len(self) == len(self.array)

    def contains(self, item: T) -> bool:
        for i in range(self.size):
            if item == self.array[i]:
                return True
        return False

    def add(self, item: T) -> None:
        if item not in self:
            if self.is_full():
                raise Exception("Set is full")

            self.array[self.size] = item
            self.size += 1

    def remove(self, item: T) -> None:
        for i in range(self.size):
            if item == self.array[i]:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                break
        else:
            raise KeyError(item)
