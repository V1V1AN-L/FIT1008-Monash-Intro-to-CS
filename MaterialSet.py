from aset import *
from material import *

class MaterialSet(ASet):
    """
    Set ADT for storing the trader's materials
    """

    def init(self, capacity: int = 1) -> None:
        super().__init__()
        self.array = ArrayR(max(1, capacity))
        
    def get_list(self) -> list[Material]:
        return [material for material in self.array if material is not None]
