"""
K’th Smallest/Largest Element in Unsorted Array:
=================================================
Given an array arr[] of size N and a number K, where K is smaller than the size of the array. Find the K’th smallest element in the given array. Given that all array elements are distinct.

Examples:  
Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
Output: 10 
"""

def smallest_element(arr, k):
    arr.sort()
    print(arr)
    id = k - 1
    return arr[id]

ele = smallest_element(arr, K)
print(f"Kth smallest element in unsorted array is: {ele}")
