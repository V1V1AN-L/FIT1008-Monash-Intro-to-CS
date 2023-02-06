""" AVL Tree implemented on top of the standard BST. """

__author__ = 'Alexey Ignatiev, with edits by Jackson Goerner'
__docformat__ = 'reStructuredText'

from bst import BinarySearchTree
from typing import TypeVar, Generic, List
from node import AVLTreeNode

K = TypeVar('K')
I = TypeVar('I')


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ Self-balancing binary search tree using rebalancing by sub-tree
        rotations of Adelson-Velsky and Landis (AVL).
    """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        BinarySearchTree.__init__(self)
        self.count = 0

    def get_height(self, current: AVLTreeNode) -> int:
        """
            Get the height of a node. Return current.height if current is
            not None. Otherwise, return 0.
            :complexity: O(1)
        """

        if current is not None:
            return current.height
        return 0

    def get_balance(self, current: AVLTreeNode) -> int:
        """
            Compute the balance factor for the current sub-tree as the value
            (right.height - left.height). If current is None, return 0.
            :complexity: O(1)
        """

        if current is None:
            return 0
        return self.get_height(current.right) - self.get_height(current.left)

    def insert_aux(self, current: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
            Inserts an item into the tree, using the key
            :complexity: O(log n)
        """
        # Find the correct location and insert the node
        if current is None:
            current = AVLTreeNode(key, item)
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')

        current.height = 1 + max(self.get_height(current.left),
                              self.get_height(current.right))

        current = self.rebalance(current)

        self.count = 0
        self.set_index(current)

        return current

    def set_index(self, root:AVLTreeNode) -> None:
        """
        Set the index of each value within the tree
        the smallest value will have the smallest index

            :complexity: O(n) because we iterate into every element

            :param root: the root tree
        """
        if root != None:
            self.set_index(root.left)
            root.index = self.count
            self.count += 1
            self.set_index(root.right)

    def delete_aux(self, current: AVLTreeNode, key: K) -> AVLTreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete.

            :Complexity: O(log n)
        """

        if current is None:
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
        else:
            if current.left is None:
                right_node = current.right
                return right_node
            elif current.right is None:
                left_node = current.left
                return left_node

        current = self.rebalance(current)
        return current

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform left rotation of the sub-tree.
            Right child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                 current                                       child
                /       \                                      /   \
            l-tree     child           -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree                 l-tree     center

            :complexity: O(1)
        """

        new_root = current.right
        center = new_root.left
        new_root.left = current
        current.right = center

        current.height = 1 + max(self.get_height(current.left),
                           self.get_height(current.right))

        new_root.height = 1 + max(self.get_height(new_root.left),
                           self.get_height(new_root.right))
        return new_root

    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform right rotation of the sub-tree.
            Left child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                       current                                child
                      /       \                              /     \
                  child       r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree

            :complexity: O(1)
        """

        new_root = current.left
        center = new_root.right
        new_root.right = current
        current.left = center

        current.height = 1 + max(self.get_height(current.left),
                                 self.get_height(current.right))

        new_root.height = 1 + max(self.get_height(new_root.left),
                                  self.get_height(new_root.right))
        return new_root


    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate
            returns the new root of the subtree.
        """
        if self.get_balance(current) >= 2:
            child = current.right
            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)
            return self.left_rotate(current)

        if self.get_balance(current) <= -2:
            child = current.left
            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)
            return self.right_rotate(current)

        return current

    def range_between(self, i: int, j: int) -> List:
        """
        Returns a sorted list of all elements in the tree between the ith and jth indices, inclusive.

        :complexity: O(j - i + log(N))
        """
        return self.range_between_aux(self.root, i, j, [])

    def range_between_aux(self, root:AVLTreeNode, i, j, result: list) -> list:
        """
        Attempts to find the value that is sorted within the index i and j
        and save it inside the result

        complexity: O(j-i + log(N))
            it happens because we don't go through into every element, we just go into the element that within the ith and jth elements which makes it O(j-i)
            Then, O(log n) comes from the recursion that happens with the depth of the tree which is log n

        :param root: the tree root
        :param i: the lower index (ith value)
        :param j: the higher index (jth value)
        :param result: the values that are located within ith and jth slot
        :return: list that consists value from ith until jth (inclusive)
        """
        if root is None:
            return result
        if root.index > i:
            self.range_between_aux(root.left, i, j, result)
        if i <= root.index <= j:
            result.append(root.item)
        if root.index < j:
            self.range_between_aux(root.right, i, j, result)
        return result