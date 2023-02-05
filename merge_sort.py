""" A simple implementation of the MergeSort algorithm. """

__author__ = 'Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from typing import List


def merge(sa1: List[float], sa2: List[float]) -> List[float]:
    """ The Merge part of the algorithm. """

    res = []  # result of merge to be stored here

    # main loop iterating through both sub-arrays simultaneously
    i, j = 0, 0
    while i < len(sa1) and j < len(sa2):
        if sa1[i] > sa2[j]:
            res.append(sa2[j])
            j += 1
        else:
            res.append(sa1[i])
            i += 1

    if i < len(sa1):
        # if there are remaining elements in sa1
        res += sa1[i:]
    elif j < len(sa2):
        # if there are remaining elements in sa2
        res += sa2[j:]

    return res


def msort(array: List[float]) -> List[float]:
    """ MergeSort implementation. Input array is split into halves. """

    if len(array) > 1:
        # computing the middle position
        mid = len(array) // 2

        # splitting array into sub-arrays and sorting them recursively
        sa1 = msort(array[:mid])
        sa2 = msort(array[mid:])

        # merging sorted sub-arrays
        return merge(sa1, sa2)
    else:
        # here is the base case of the recursion (nothing to sort!)
        return array

