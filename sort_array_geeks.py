"""
Sort in specific order:
======================
Sort all even numbers in ascending order and then sort all odd numbers in descending order
Given an array of integers (both odd and even), sort them in such a way that the first part of the array contains odd numbers sorted in descending order, rest portion contains even numbers sorted in ascending order.
Examples: 

Input: arr[] = {1, 2, 3, 5, 4, 7, 10}
Output: arr[] = {7, 5, 3, 1, 2, 4, 10}

Input: arr[] = {0, 4, 5, 3, 7, 2, 1}
Output: arr[] = {7, 5, 3, 1, 0, 2, 4} 

Link: https://www.geeksforgeeks.org/sort-even-numbers-ascending-order-sort-odd-numbers-descending-order/
"""
def sort(arr):
    even = []
    odd = []
    arr = sorted(arr)
    for i in range(len(arr)):
        if (arr[i] % 2) == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    odd = odd[::-1]
    odd.extend(even)   
    return odd

op = sort(arr)
print(f"Final sorted array is :{op}")
