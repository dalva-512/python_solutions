"""
Array Duplicates:
=================
Given an array arr of integers, find all the elements that occur more than once in the array. Return the result in ascending order. If no element repeats, return an empty list.

Examples:
Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.

Input: arr[] = [0, 3, 1, 2] 
Output: [] 
Explanation: There is no repeating element in the array, so the output is empty.

Input: arr[] = [2]
Output: [] 
Explanation: There is single element in the array. Therefore output is empty.

Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 106

Link: https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1?page=1&company=Amazon&sortBy=submissions 
"""
class Solution:
    def array_dup(self, arr):
        dup_ar = dict()
        cnt = 0
        ret = []
        for i in arr:
            cnt = arr.count(i)
            dup_ar[i] = cnt
        for key, val in dup_ar.items():
            if val > 1:
                ret.append(key)
        return ret

arr = [0, 3, 1, 2] 
sol = Solution()
ret_ar = sol.array_dup(arr)
print(ret_ar)

# Using Counter:
from collections import Counter
class Solution:
    
    def findDuplicates(self, arr):
        res = []
        cnt = Counter(arr)
        for k, v in cnt.items():
            if v > 1:
                res.append(k)
        return res if res else []

# Other method: O(n) complexity
class Solution:

    def findDuplicates(self, arr):
        # Dictionary to store the frequency of elements
        freq = {}

        # Count the frequency of each element in the array
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # List to store the result (duplicates)
        result = []

        # Check for elements that occur more than once
        for key, value in freq.items():
            if value > 1:
                result.append(key)

        # If no duplicates are found, return an empty list
        return result if result else []
