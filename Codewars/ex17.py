# Find the odd int
#
# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
# Examples
#
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    for e in seq:
        x = seq.count(e)
        if x % 2:
            return e

def find_itfast(seq):
    return [e for e in seq if seq.count(e) % 2][0]
#The [0] at the end of the list comprehension selects the first element of the filtered list

import operator
from functools import reduce
def find_itgenius(xs):
     return reduce(operator.xor, xs)

# A list like [1, 2, 3, 1, 2, 3, 4] can be thought of as [1, 1, 2, 2, 3, 3, 4].
# 1 xor 1 = 0
# 0 xor 2 = 2
# 2 xor 2 = 0

import unittest
class testex16(unittest.TestCase):
    def test_ex16(self):
            self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
            self.assertEqual(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
            self.assertEqual(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)