"""
First and Second Smallests:
===========================
Difficulty: BasicAccuracy: 24.44%Submissions: 124K+Points: 1
Given an array, arr of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: 2 3 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
Input: arr[] = [1, 1, 1]
Output: -1
Explanation: Only element is 1 which is smallest, so there is no second smallest element.
Link: https://www.geeksforgeeks.org/problems/find-the-smallest-and-second-smallest-element-in-an-array3226/1 
"""
class Solution:
    def minAnd2ndMin(self, arr):
        st = set(arr)
        if len(st) == 1:
            return [-1, -1] 
        mn = sorted(st)[0]
        mns = sorted(st)[1]
        return [mn, mns]
        
