"""
Given an array arr of integers, find all the elements that occur more than once in the array. If no element repeats, return an empty array.

Examples:

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.
Input: arr[] = [0, 3, 1, 2] 
Output: [] 
Explanation: There is no repeating element in the array, so the output is empty.
Input: arr[] = [2]
Output: [] 
Explanation: There is single element in the array. Therefore output is empty.
Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 106

Link: https://www.geeksforgeeks.org/problems/second-largest3735/
"""
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) == 1:
            return -1
        s1 = set(arr)
        if len(s1) == 1:
            return -1
        ar = sorted(list(s1))
        return ar[-2]
