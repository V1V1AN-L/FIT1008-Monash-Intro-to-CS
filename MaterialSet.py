from aset import *
from material import *
from merge_sort import *
from avl import *

class MaterialSet(ASet):
    """
    Set ADT for storing the trader's materials
    Built from an array set
    """

    def __init__(self, capacity: int = 1, items: list[Material] = None) -> None:
        ASet.__init__(self)
        self.array = ArrayR(max(1, capacity))
        if isinstance(items, list):
            for material in items:
                self.add(material)
        
    def get_list(self) -> list[Material]:
        """
        returns a list of the trader's materials    
        """
        
        return self.array.array[:self.size]
    
    def add(self, item: T) -> None:
        """ Adds an element to the set. Note that an element already
        present in the set should not be added.
        :pre: the set is not full
        """
        if self.is_full():
            self.refactor_array()
        if item not in self:
            self.array[self.size] = item
            self.size += 1
            
            
    def refactor_array(self):
        """
        resizes the array to fit more materials
        """
        old_array = self.array
        new_array = ArrayR(len(old_array) + 10)
        self.array = new_array
        for i in range(len(old_array)):
            self.array[i] = old_array[i]


class MaterialAVL(AVLTree):
    """
    AVL tree for use in Range trader. Stores materials based on their mining difficulty
    """
    def __init__(self, capacity: int = 1, items: list[Material] = None) -> None:
        AVLTree.__init__(self)
        self.tree = AVLTree()
        if isinstance(items, list):
            for material in items:
                self.add(material)

    def add(self, item: Material) -> None:
        """
        Adds an element to the tree.
        """
        self.tree[item.mining_rate] = item

    def get_list(self) -> list[Material]:
        """
        returns a list of the trader's materials using inorder traversal of the avl tree
        """
        node_list = []
        for item in self.tree:
            node_list.append(item)
        return node_list






if __name__ == '__main__':
    # MS = MaterialSet(8,["Stone","Cobblestone","Stone Bricks","Stone Slabs","Stone stairs","Furnace"])
    # MS.add("Stone Wall")
    # print(MS.get_list())
    class quick_mat:
        def __init__(self, mr):
            self.mining_rate = mr

    stone = quick_mat(1)
    cobblestone = quick_mat(2)
    stone_slab = quick_mat(0.5)
    stone_brick = quick_mat(-2)
    stone_stairs = quick_mat(3)

    MS = MaterialAVL(8,[stone,cobblestone,stone_slab,stone_stairs])
    MS.add(stone_brick)

    print(MS.get_list())