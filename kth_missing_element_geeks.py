"""
K-th missing element:
=========================
Given an increasing sequence arr, we need to find the K-th smallest missing element, taking the first element of the array as the starting point in the increasing sequence. If there is no k-th missing element then output -1.

Example:

Input: arr[] = [1, 3, 4, 5, 7] and k = 2
Output: 6
Explanation: k = 2, Missing numbers are 2 and 6. So 2nd missing number is 6.
Input: arr[] = [2, 3, 4, 5, 6, 8] and k = 1
Output: 7
Explanation: k = 1, the first missing number in the array is 7.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤  arr.size() ≤ 106
0 ≤  k, arr[i] ≤ 105

Link: https://www.geeksforgeeks.org/problems/k-th-missing-element3635/1?page=1&company=Apple&difficulty=Basic,Easy&sortBy=submissions
"""

arr = [2, 3, 4, 5, 6, 8] 
k = 1

def missing_num(arr, k):
    res = []
    j = 0
    for i in range(len(arr)):
        j += 1
        if j != arr[i]:
            res.append(j)
            j = arr[i]

    if k >= 1:
        return res[1]
    else:
        return -1

val = missing_num(arr, k)
print(val)
        
