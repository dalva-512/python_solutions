"""
Check for Binary String:
=========================
Difficulty: BasicAccuracy: 30.94%Submissions: 127K+Points: 1
Given a non-empty sequence of characters s, return true if sequence is Binary, else return false.

Examples:

Input: s = "101"
Output: true
Explanation: Since string contains only '0' and '1', output is true.
Input: s = "75"
Output: false
Explanation: Since string contains digits other than '0' and '1', output is false.
Link: https://www.geeksforgeeks.org/problems/check-for-binary/1?page=4&category=Arrays,Strings&difficulty=Basic,Easy&sortBy=submissions
"""
class Solution:
    def isBinary(self, s):
        if not s.isdigit():
            return False
        l = list(s)
        for i, n in enumerate(l):
            n = int(n)
            if n != 1 and n != 0:
                return False
        return True
