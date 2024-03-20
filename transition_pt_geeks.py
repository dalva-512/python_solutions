"""
Find the transition point in a binary array:
============================================
Given a sorted array containing only numbers 0 and 1, the task is to find the transition point efficiently. The transition point is the point where “0” ends and “1” begins.

Examples : 
Input: 0 0 0 1 1
Output: 3
Explanation: Index of first 1 is 3

Input: 0 0 0 0 1 1 1 1
Output: 4
Explanation: Index of first 1 is 4

Link: https://www.geeksforgeeks.org/find-transition-point-binary-array/
"""

def transition_point(arr: list) -> int:
    for i in range(len(arr)):
        if arr[i] == 1:
            return i
   
pt = transition_point(arr)
print(f"Index of first 1 is {pt}")
