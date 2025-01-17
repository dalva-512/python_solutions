"""
Number of occurrence:
=====================
Difficulty: EasyAccuracy: 59.34%Submissions: 286K+Points: 2
Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

Examples :

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.
Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ target ≤ 106

Link: https://www.geeksforgeeks.org/problems/number-of-occurrence2259
"""
# Solution 1:
from collections import Counter
class Solution:
    def countFreq(self, arr, target):
        dct = Counter(arr)
        for k, v in dct.items():
            if k == target:
                return v
        else:
            return 0

#Solution 2:
# Python program to find the occurrence of given
# target using linear search

def countFreq(arr, target):
    res = 0
    for i in range(len(arr)):
      
        # If the current element is equal to 
        # target, increment the result
        if arr[i] == target:
            res += 1

    return res

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(countFreq(arr, target))
