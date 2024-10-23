"""
Missing in Array
Difficulty: EasyAccuracy: 29.59%Submissions: 1.2MPoints: 2
You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.

https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&company=Amazon&sortBy=submissions
"""
class Solution:
    def miss_array(self, arr):
        for i in range(len(arr)):
            j = i + 1
            if j != arr[i]:
                return j
        

arr = [1, 2, 3, 5]
sol = Solution()
val = sol.miss_array(arr)
print(val)
