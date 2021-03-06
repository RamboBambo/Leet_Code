import unittest
from typing import *
# tags:

# Time = O(N)
# Space = O(N)
class Solution:
    '''
    A = [0,1,3,50,75]
    lower = 0
    upper = 100

    set previous to lower -1
    3 cases:
    if current is exactly 2 more than previous -> append single number
    if current is is more than previous + 2 -> append range
    if current is 1 more than previous -> do nothing

    single number = current-1
    range = prev+1 -> current-1

    '''
    def findMissingRanges(self, A, lower, upper):
        result = []
        A.append(upper+1)

        pre = lower - 1 #tip: calculate this last
        for i in A:
            if (i == pre + 2):
                result.append(str(i-1))
            elif (i > pre + 2):
                result.append(str(pre + 1) + "->" + str(i -1))
            pre = i
        return result

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        nums = [0, 1, 3, 50, 75]
        lower = 0
        upper = 99
        s = Solution()
        self.assertEqual(s.findMissingRanges(nums, lower, upper), ["2", "4->49", "51->74", "76->99"])

    def test_simple2(self):
        nums = []
        lower = 1
        upper = 1
        s = Solution()
        self.assertEqual(s.findMissingRanges(nums, lower, upper), ['1'])

    def test_simple2(self):
        nums = [-1]
        lower = -2
        upper = -1
        s = Solution()
        self.assertEqual(s.findMissingRanges(nums, lower, upper), ['-2'])


if __name__ == "__main__":
	unittest.main()
