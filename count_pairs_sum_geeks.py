"""
Count Pairs in a sorted array whose sum is less than target:
============================================================
Difficulty: EasyAccuracy: 41.4%Submissions: 396+Points: 2
Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target.

Examples:

Input: arr[] = [2, 3, 5, 7], target = 8
Output: 2
Explanation: The pairs are (2, 3) and (2, 5).
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], target = 7
Output: 6
Explanation: The pairs are (1, 2), (1, 3), (1, 4), (1, 5), (2, 3) and (2, 4)
Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 104
1 <= target <= 104

Link: https://www.geeksforgeeks.org/problems/count-pairs-in-a-sorted-array-whose-sum-is-less-than-target/
"""
class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        cnt = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] < target:
                    cnt += 1
        return cnt
# Solution 2: https://www.geeksforgeeks.org/count-pairs-array-whose-sum-less-x/
