"""
Check Equal Arrays:
=======================
Difficulty: EasyAccuracy: 42.18%Submissions: 375K+Points: 2
Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.

Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.

Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

Examples:

Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
Output: true
Explanation: Both the array can be rearranged to [0,1,2,4,5]
Input: a[] = [1, 2, 5], b[] = [2, 4, 15]
Output: false
Explanation: a[] and b[] have only one common value.
Constraints:
1<= a.size(), b.size()<=107
0<=a[i], b[i]<=109

Link: https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/
"""
# User function Template for python3

from collections import Counter
class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        s1 = Counter(a)
        s2 = Counter(b)
        
        for i, n in s1.items():
            for j, k in s2.items():
                if i not in b or j not in a:
                    return False
                if i == j and n != k:
                    return False
        else:
            return True
            
            
