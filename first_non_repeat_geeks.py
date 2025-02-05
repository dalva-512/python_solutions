"""
Non-Repeating Element:
=======================
Difficulty: EasyAccuracy: 39.31%Submissions: 120K+Points: 2Average Time: 20m
Find the first non-repeating element in a given array arr of integers and if there is not present any non-repeating element then return 0

Note: The array consists of only positive and negative integers and not zero.

Examples:

Input: arr[] = [-1, 2, -1, 3, 2]
Output: 3
Explanation: -1 and 2 are repeating whereas 3 is the only number occuring once. Hence, the output is 3. 
Input: arr[] = [1, 1, 1]
Output: 0
Explanation: There is not present any non-repeating element so answer should be 0.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= arr.size <= 106
-109 <= arr[i] <= 109
arr[i] != 0 

Link: https://www.geeksforgeeks.org/problems/non-repeating-element3958/
"""
#User function Template for python3
from collections import Counter
class Solution:
    def firstNonRepeating(self, arr): 
        dct = Counter(arr)
        for k, v in dct.items():
            if v == 1:
                return k
        else:
            return 0
        
