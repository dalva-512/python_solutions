"""
Find Transition Point:
======================
Given a sorted array, arr[] containing only 0s and 1s, find the transition point, i.e., the first index where 1 was observed, and before that, only 0 was observed.  If arr does not have any 1, return -1. If array does not have any 0, return 0.

Examples:

Input: arr[] = [0, 0, 0, 1, 1]
Output: 3
Explanation: index 3 is the transition point where 1 begins.
Input: arr[] = [0, 0, 0, 0]
Output: -1
Explanation: Since, there is no "1", the answer is -1.
Input: arr[] = [1, 1, 1]
Output: 0
Explanation: There are no 0s in the array, so the transition point is 0, indicating that the first index (which contains 1) is also the first position of the array.
Input: arr[] = [0, 1, 1]
Output: 1
Explanation: Index 1 is the transition point where 1 starts, and before it, only 0 was observed.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 1

Link: https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1
"""
class Solution:
    def transitionPoint(self, arr):
        if 1 not in arr:
            return -1
            
        if 0 not in arr:
            return 0
        for i in range(len(arr) + 1):
            j = i + 1
            if arr[i] == 0 and arr[j] == 1:
                return j
