"""
Two sum -Pairs with 0 Sum
Difficulty: EasyAccuracy: 31.49%Submissions: 464K+Points: 2
Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

Examples:

Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, 1]]
Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
arr[2] + arr[4] = 1 + (-1) = 0.
The distinct pair are [-1,1].
Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
Output: [[-6, 6],[-1, 1]]
Explanation: The distinct pairs are [-1, 1] and [-6, 6].
Expected Time Complexity: O(n log n)
Expected Auxiliary Space: O(n).

Constraints:
3 <= arr.size <= 105
-105 <= arr[i] <= 105
Link: https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1?page=1&difficulty=Basic,Easy&sortBy=submissions
"""
class Solution:
    def getPairs(self, arr):
        res = []
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):  # Fix to start j from i + 1 to avoid duplicate checks
                if arr[i] + arr[j] == 0:
                    pair = sorted([arr[i], arr[j]])  # Sort pair to handle duplicates
                    if pair not in res:
                        res.append(pair)
        return res

arr = [-1, 0, 1, 2, -1, -4]
sol = Solution()
res = sol.getPairs(arr)
print(res)
