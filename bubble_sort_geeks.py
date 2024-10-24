"""
Sort 0s, 1s and 2s
Difficulty: EasyAccuracy: 50.58%Submissions: 708K+Points: 2
Given an array arr containing only 0s, 1s, and 2s. Sort the array in ascending order.

Examples:

Input: arr[] = [0, 2, 1, 2, 0]
Output: [0, 0, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Input: arr[] = [0, 1, 0]
Output: [0, 0, 1]
Explanation: 0s 1s and 2s are segregated into ascending order.

Input: arr[] = [2, 2, 2]
Output: [2, 2, 2]
Explanation: Only 2s are present here.
Link: https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1?page=1&company=Amazon&sortBy=submissions
"""
class Solution:
    def sort_ar(self, arr):
        for i in range(len(arr) -1, 0 , -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
        

arr = [0, 2, 1, 2, 0]
sol = Solution()
ret_ar = sol.sort_ar(arr)
print(ret_ar)
