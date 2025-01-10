"""
Palindromic Array:
==================
Difficulty: BasicAccuracy: 58.62%Submissions: 174K+Points: 1
Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.

Examples:

Input: arr[] = [111, 222, 333, 444, 555]
Output: true
Explanation:
arr[0] = 111, which is a palindrome number.
arr[1] = 222, which is a palindrome number.
arr[2] = 333, which is a palindrome number.
arr[3] = 444, which is a palindrome number.
arr[4] = 555, which is a palindrome number.
As all numbers are palindrome so This will return true.
Input: arr[] = [121, 131, 20]
Output: false
Explanation: 20 is not a palindrome hence the output is false.
Expected Time Complexity: O(nlogn)
Expected Space Complexity: O(1)

Constraints:
1 <=arr.size<= 20
1 <=arr[i]<= 105

Link: https://www.geeksforgeeks.org/problems/palindromic-array-1587115620/
"""
# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    for i in range(len(arr)):
        n = str(arr[i])
        l = n[::-1]
        if n != l:
            return False
    
    return True
