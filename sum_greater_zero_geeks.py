"""
Number of pairs in an array with the sum greater than 0:
=======================================================
Given an array arr[] of size N, the task is to find the number of distinct pairs in the array whose sum is > 0.

Examples: 
Input: arr[] = { 3, -2, 1 } 
Output: 2 
Explanation: 
There are two pairs of elements in the array whose sum is positive. They are: 
{3, -2} = 1 
{3, 1} = 4

Input: arr[] = { -1, -1, -1, 0 } 
Output: 0 
Explanation: 
There are no pairs of elements in the array whose sum is positive. 
"""
def array_sum(arr: list) -> int:
    sm = 0
    op = []
    for i in range(len(arr) -1):
        for j in range(1, len(arr)):
            sm = arr[i] + arr[j]
            if sm > 0:
                op.append(sm)
    ln = len(op)
    return ln

                
val = array_sum(arr)
if val > 0:
    print(f"There are {val} pairs of elements in the array whose sum is positive.")
else:
    print("There are no pairs of elements in the array whose sum is positive.")
