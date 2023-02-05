from primes import *

""" Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
"""
# from __future__ import annotations
__author__ = 'Brendon Taylor. Modified by Graeme Gange, Alexey Ignatiev, and Jackson Goerner'
__docformat__ = 'reStructuredText'
__modified__ = '21/05/2020'
__since__ = '14/05/2020'

from referential_array import ArrayR
from typing import TypeVar, Generic

T = TypeVar('T')


class LinearProbeTable(Generic[T]):
    MIN_CAPACITY = 1
    """
        Linear Probe Table.

        attributes:
            count: number of elements in the hash table
            table: used to represent our internal array
            tablesize: current size of the hash table

            probe_total: total distance of probe when inserting a new value
            probe_max: maximum of distance of probe when inserting a new value compared with the others.
            rehash_count: number of rehashing method called
    """

    def __init__(self, expected_size: int, tablesize_override: int = -1) -> None:
        """
            Initialiser.
        """

        self.conflict_count = 0
        self.probe_total = 0
        self.probe_max = 0
        self.rehash_count = 0
        if tablesize_override == -1:
            prime_tablesize = LargestPrimeIterator(expected_size, 2)
            self.table_size = next(prime_tablesize)
        else:
            self.table_size = tablesize_override

        self.count = 0
        self.table = ArrayR(max(self.MIN_CAPACITY, self.table_size))

    def hash(self, key: str) -> int:
        """
            Hash a key for insertion into the hashtable.
        """

        value = 0
        a = 31415
        b = 27183
        for char in key:
            value = (ord(char) + a * value) % self.table_size
            a = a * b % (self.table_size - 1)
        return value

    def get_load_factor(self) -> float:
        """
        Calculate the load factor
        by calculate the total probe that will happens in the hash table
        and divide it by the table_size

        :return: the value of laod factor
        """
        probe = 0
        for index in range(self.table_size):
            count = 0
            pos = index
            while self.table[pos] is not None:
                pos = (pos + 1) % self.table_size
                count += 1
                if pos == index:
                    break
            probe += count
        return probe / self.table_size

    def statistics(self) -> tuple:
        '''
        Return:
        1. conflict_count: total number of conflicts (two or more values have the same key value)
        2. probe_total: total probe_chain throughout the hash table
        3. probe_max: longest probe chain
        4. rehash_count: how many rehashing has been done if the load factor is > 0.5
        '''

        return (self.conflict_count, self.probe_total, self.probe_max, self.rehash_count)

    def __len__(self) -> int:
        """
            Returns number of elements in the hash table
            :complexity: O(1)
        """
        return self.count

    def _linear_probe(self, key: str, is_insert: bool) -> int:
        """
            Find the correct position for this key in the hash table using linear probing
            :complexity best: O(K) first position is empty
                            where K is the size of the key
            :complexity worst: O(K + N) when we've searched the entire table
                            where N is the tablesize
            :raises KeyError: When a position can't be found
        """
        position = self.hash(key)  # get the position using hash
        probe_temp = self.probe_total
        conflict_temp = self.conflict_count

        if is_insert and self.is_full():
            raise KeyError(key)

        for _ in range(len(self.table)):  # start traversing
            if self.table[position] is None:  # found empty slot
                if is_insert:
                    return position
                else:
                    raise KeyError(key)  # so the key is not in
            elif self.table[position][0] == key:  # found key
                return position
            else:  # there is something but not the key, try next
                position = (position + 1) % len(self.table)
                self.probe_total += 1
                self.probe_max = max(self.probe_max, self.probe_total - probe_temp)
                if self.conflict_count == conflict_temp:
                    self.conflict_count += 1

        raise KeyError(key)

    def keys(self) -> list[str]:
        """
            Returns all keys in the hash table.
        """
        res = []
        for x in range(len(self.table)):
            if self.table[x] is not None:
                res.append(self.table[x][0])
        return res

    def values(self) -> list[T]:
        """
            Returns all values in the hash table.
        """
        res = []
        for x in range(len(self.table)):
            if self.table[x] is not None:
                res.append(self.table[x][1])
        return res

    def __contains__(self, key: str) -> bool:
        """
            Checks to see if the given key is in the Hash Table
            :see: #self.__getitem__(self, key: str)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> T:
        """
            Get the item at a certain key
            :see: #self._linear_probe(key: str, is_insert: bool)
            :raises KeyError: when the item doesn't exist
        """
        position = self._linear_probe(key, False)
        return self.table[position][1]

    def __setitem__(self, key: str, data: T) -> None:
        """
            Set an (key, data) pair in our hash table
            :see: #self._linear_probe(key: str, is_insert: bool)
            :see: #self.__contains__(key: str)
        """
        if self.get_load_factor() > 1.2:
            self._rehash()

        position = self._linear_probe(key, True)

        if self.table[position] is None:
            self.count += 1

        self.table[position] = (key, data)

    def is_empty(self):
        """
            Returns whether the hash table is empty
            :complexity: O(1)
        """
        return self.count == 0

    def is_full(self):
        """
            Returns whether the hash table is full
            :complexity: O(1)
        """
        return self.count == len(self.table)

    def insert(self, key: str, data: T) -> None:
        """
            Utility method to call our setitem method
            :see: #__setitem__(self, key: str, data: T)
        """
        self[key] = data

    def _rehash(self) -> None:
        """
            Need to resize table and reinsert all values
        """
        new_hash = LinearProbeTable(self.table_size * 2)

        for i in range(len(self.table)):
            if self.table[i] is not None:
                new_hash[str(self.table[i][0])] = self.table[i][1]

        self.count = new_hash.count
        self.table = new_hash.table
        self.table_size = new_hash.table_size
        self.rehash_count += 1

    def __str__(self) -> str:
        """
            Returns all they key/value pairs in our hash table (no particular
            order).
            :complexity: O(N) where N is the table size
        """
        result = ""
        for item in self.table:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result
