from aset import *
from material import *

class MaterialSet(ASet):
    """
    Set ADT for storing the trader's materials
    """

    def init(self, capacity: int = 1, items: list[Material] = None) -> None:
        ASet.__init__(self)
        self.array = ArrayR(max(1, capacity))
        if isinstance(items, list):
            for material in items:
                self.add(material)
        
    def get_list(self) -> list[Material]:
        return self.array.array[:self.size]
