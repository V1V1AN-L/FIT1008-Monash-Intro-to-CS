from aset import *
from material import *

class MaterialSet(ASet):
    """
    Set ADT for storing the trader's materials
    """

    def __init__(self, capacity: int = 1, items: list[Material] = None) -> None:
        ASet.__init__(self)
        self.array = ArrayR(max(1, capacity))
        if isinstance(items, list):
            for material in items:
                self.add(material)
        
    def get_list(self) -> list[Material]:
        return self.array.array[:self.size]
    
    def add(self, item: T) -> None:
        """ Adds an element to the set. Note that an element already
        present in the set should not be added.
        :pre: the set is not full
        :raises Exception: if the set is full.
        """
        if self.is_full():
            self.refactor_array()
        if item not in self:
            self.array[self.size] = item
            self.size += 1
            
            
    def refactor_array(self):
        # refactor array
        old_array = self.array
        new_array = ArrayR(len(old_array) + 10)
        self.array = new_array
        for i in range(len(old_array)):
            self.array[i] = old_array[i]