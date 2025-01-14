"""
Palindrome String:
=================
Difficulty: EasyAccuracy: 51.21%Submissions: 373K+Points: 2
You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

Examples :

Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
Input: s = "a"
Output: true
Explanation: A single-character string is always a palindrome.
Input: s = "acbca"
Output: true
Explanation: "acbca" reads the same forwards and backwards, so it is a palindrome.
Constraints:
1 ≤ s.size() ≤ 106
The string s contains only lowercase letters (a-z).

Link: https://www.geeksforgeeks.org/problems/palindrome-string0817
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]  # Check if the string is equal to its reverse.
