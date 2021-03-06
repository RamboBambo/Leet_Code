#------------------------------------------------------------------------------
# Question: 0937_reorder_data_in_log_files.py
#------------------------------------------------------------------------------
# tags: Easy
'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.
Then, either:
Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the
identifier used in case of ties.  The digit-logs should be put in their original
order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

'''
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time: O(nlogn) where n is number of logs
    Space: O(n)
    '''
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def isDigit(log):
            return log.split()[1].isdigit()

        lets = [x for x in logs if not isDigit(x)]
        digits = [x for x in logs if isDigit(x)]
        lets.sort()
        lets.sort(key=lambda x: x.split()[1:])
        result = lets + digits

        return lets + digits

class Solution2:
    '''
    Time: O(nlogn) where n is number of logs
    Space: O(n)
    '''
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f (log):
            identifier, content = log.split(" ", 1) # 1 denotes maximum number of splits
            return (0, content, identifier) if content[0].isalpha() else (1,)
        return sorted(logs, key=f)


class SolutionQuickSort:
    def quick_sort(self, logs):
        '''
        ["let1 art","let3 art","let2 art own dig","dig1 8 1 5 1","dig2 3 6"]
        '''
        def cmp(a, b):
            #return true if a < b
            z = list(zip(a,b))
            n = len(z)
            for i in range(1, n):
                if z[i][0] < z[i][1]:
                    return True
                if z[i][0] > z[i][1]:
                    return False
            if len(a) > len(b):
                return False
            else:
                return a[0] <= b[0]

        def partition(left, right):
            pValue = logs[right]
            pIndex = left
            for i in range(left, right):
                if cmp(logs[i], pValue):
                    logs[pIndex], logs[i] = logs[i], logs[pIndex]
                    pIndex += 1
            logs[right], logs[pIndex] = logs[pIndex], logs[right]
            return pIndex

        def helper(left, right):
            if left < right:
                pivot = partition(left, right)
                helper(left, pivot-1)
                helper(pivot+1, right)

        helper(0, len(logs)-1)

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        d = ["dig1...", "dig2..."]
              ^
             [dig1, 8, 1, 5, 1]

        l = ["let1...", "let2..."]
              ^
        convert to array [[let, art, can], [let2, ow, kit, dig]]
        custom sort key function

        f(a:) -> key to sort by
          zip a, b
          compare from idx=1 -> end
          return true if a >  b        #> means lexographically in front
          else if a < b: return false
        if all words are equal: use the identifier
        '''

        d = [d for d in logs if d[0] == 'd']
        l = [l.split(' ') for l in logs if l[0] == "l"]
        self.quick_sort(l)
        l = [" ".join(x) for x in l]
        l.extend(d)
        return l

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        s = Solution()
        self.assertEqual(
            s.reorderLogFiles(logs),
            ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])

        s = Solution2()
        self.assertEqual(
            s.reorderLogFiles(logs),
            ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])


    def test_letter_ties(self):
        logs = ["dig1 8 1 5 1","let3 art","dig2 3 6","let2 art own dig","let1 art"]
        s = Solution()
        self.assertEqual(
            s.reorderLogFiles(logs),
            ["let1 art","let3 art","let2 art own dig","dig1 8 1 5 1","dig2 3 6"])


        s = Solution2()
        self.assertEqual(
            s.reorderLogFiles(logs),
            ["let1 art","let3 art","let2 art own dig","dig1 8 1 5 1","dig2 3 6"])

    def test_simple2(self):
        logs = ["let1 act","let8 act aoo"]

        s = Solution2()
        self.assertEqual(s.reorderLogFiles(logs), ["let1 act", "let8 act aoo"])
unittest.main(verbosity=2)

