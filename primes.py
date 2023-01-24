""" Task one iterator function"""

from __future__ import annotations
from Sieve_of_Sundaram_prime import * #has max at 10000 currently needs change

__author__ = 'Forbes Purcell'
__docformat__ = 'reStructuredText'

class LargestPrimeIterator():
    """ iterator that yields largest prime less than upper_bound"""
    def __init__(self, upper_bound, factor):
        self.upper_bound = upper_bound
        self.factor = factor
        Sieve()


    def __iter__(self):
        return self

    def __next__(self):
        """ return the largest prime less than upper_bound
            set upper bound to prime*factor"""
        prime = get_highest_prime(self.upper_bound)
        self.upper_bound = prime * self.factor

        return prime


if __name__ == "__main__":
    test = LargestPrimeIterator(6,2)
    for i in range(0,23):
        print(next(test))