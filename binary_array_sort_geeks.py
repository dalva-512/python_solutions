"""
Binary Array Sorting:
=====================
Difficulty: BasicAccuracy: 53.94%Submissions: 121K+Points: 1Average Time: 20m
You are given a binary array arr[], where each element is either 0 or 1. Your task is to rearrange the array in increasing order in place (without using extra space). You do not need to return anything; simply modify the input array.

Examples:

Input: arr[] = [1, 0, 1, 1, 0]
Output: [0, 0, 1, 1, 1]
Explanation: After arranging the elements in increasing order, elements will be as 0 0 1 1 1.
Input: arr[] = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
Output: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
Explanation: After arranging the elements in increasing order, elements will be 0 0 0 0 1 1 1 1 1 1.
Input: arr[] = [1, 1, 1, 1]
Output: [1, 1, 1, 1]
Explanation: Since the array already contains only 1s, no change is needed.

Link: https://www.geeksforgeeks.org/problems/binary-array-sorting-1587115620/1
"""

class Solution:
    # Function to sort the binary array in non-decreasing order
    def binSort(self, arr):
        for i in range(len(arr) -1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
