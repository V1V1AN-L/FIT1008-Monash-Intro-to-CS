""" Task one iterator function"""

from __future__ import annotations

__author__ = 'Zecan Liu'
__docformat__ = 'reStructuredText'

class LargestPrimeIterator():
    """ iterator that yields largest prime less than upper_bound"""
    def __init__(self, upper_bound, factor):
        self.upper_bound = upper_bound
        self.factor = factor

    def __iter__(self):
        return self

    def __next__(self):
        """ return the largest prime less than upper_bound
            set upper bound to prime*factor"""
        prime = self.upper_bound
        while not is_prime(prime):
            prime -= 1
        self.upper_bound = prime * self.factor
        return prime


def is_prime(n: int) -> bool:
    """
    This function is copied from Week 9 Applied - Counting Primes

    Checks whether n is prime or not.
    Returns true if prime, false otherwise.
    """
    # These checks work for up to 2^32.
    vals = [2, 7, 61]

    if n < 2:
        return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for v in vals:
        if v >= n:
            break
        x = pow(v, d, n)
        if x == 1 or x == n-1:
            continue
        good = False
        for r in range(1, s):
            x = (x*x) % n
            if x == n-1:
                good = True
                break
        if not good:
            return False
    return True


if __name__ == "__main__":
    test = LargestPrimeIterator(6,2)
    for i in range(0,23):
        print(next(test))