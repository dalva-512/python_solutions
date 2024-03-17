"""
Program for array left rotation by d positions.
==================================================
Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.

Examples:  
Input: 
arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
Output: 3 4 5 6 7 1 2

Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
Output: 5 6 7 1 2 3 4

Link: https://www.geeksforgeeks.org/array-rotation/
"""
def rotate_d_pos(arr1, d):
    final = []
    last = []
    last = arr1[:d]
    final = arr1[d:]
    final.extend(last)
    return final

op = rotate_d_pos(arr1, d)
print(op)
