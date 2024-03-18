"""
Find subarray with given sum:
==============================
Find Subarray with given sum | Set 1 (Non-negative Numbers)
Given an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.

Note: There may be more than one subarray with sum as the given sum, print first such subarray. 

Examples: 

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33
"""
def subarray_sum(arr, sm):
    ln = len(arr)
    for i in range(len(arr) - 2):
        for j in range(1, len(arr) -1):
            for k in range(2, len(arr)):
                addtn = arr[i] + arr[j] + arr[k]
                if addtn == sm:
                    return i, k
    else:
        return -1, -1

start, end = subarray_sum(arr, sm)
print(f"Sum found between indexes {start} and {end}")
