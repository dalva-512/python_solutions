"""
Missing in Array:
================
Difficulty: EasyAccuracy: 29.59%Submissions: 1.3MPoints: 2
You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.
Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.
Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size() + 1

Link: https://www.geeksforgeeks.org/problems/missing-number-in-array1416/
"""
class Solution:
    def missingNumber(self, arr):
        # Filter positive numbers and sort them
        ar = sorted(x for x in arr if x > 0)
        ln = len(ar)
        
        # Check for the missing number
        for i in range(ln):
            if ar[i] != i + 1:
                return i + 1
        
        # If all numbers are sequential, the missing number is the next one
        return ln + 1

# Example Input
arr = [2, 1]
sol = Solution()
res = sol.missingNumber(arr)
print(res)

"""
Explanation:
Filtering and Sorting:

The array is filtered to keep only positive integers (x > 0) since the problem assumes we are finding the smallest positive missing number.
Checking for Missing Numbers:

Loop through the sorted array, comparing each element with its expected value (i + 1).
If there's a mismatch, return the missing value.
Default Return:

If all numbers are sequential, the missing number is the next one (ln + 1).

"""
