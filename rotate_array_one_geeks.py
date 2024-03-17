"""
Program to cyclically rotate an array by one:
=============================================
Given an array, the task is to cyclically rotate the array clockwise by one time. 

Examples:  

Input: arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}

Input: arr[] = {2, 3, 4, 5, 1}
Output: {1, 2, 3, 4, 5}


Link: https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/
"""
def rotate_one(arr1):
    final = []
    last = arr1[-1]
    final = arr1[:-1]
    final.insert(0, last)
    return final

op = rotate_one(arr1)
print(op)
