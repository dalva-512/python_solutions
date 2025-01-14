"""
Two Sum - Pair with Given Sum:
=============================
Difficulty: EasyAccuracy: 30.61%Submissions: 342K+Points: 2
Given an array arr[] of positive integers and another integer target. Determine if there exists two distinct indices such that the sum of there elements is equals to target.

Examples:

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 16
Output: true
Explanation: arr[3] + arr[4] = 6 + 10 = 16.
Input: arr[] = [1, 2, 4, 3, 6], target = 11
Output: false
Explanation: None of the pair makes a sum of 11.
Input: arr[] = [11], target = 11
Output: false
Explanation: No pair is possible as only one element is present in arr[].
Constraints:
1 ≤ arr.size ≤ 105
1 ≤ arr[i] ≤ 105
1 ≤ target ≤ 2*105

Link: https://www.geeksforgeeks.org/problems/key-pair5616/1?
"""
#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
	    res = dict()
	    
	    for idx, num in enumerate(arr):
	        compliment = target - num
	        if compliment in res:
	            return True
	        res[num] = idx
	    return False
