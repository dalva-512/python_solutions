"""
Non Repeating Character:
========================
Difficulty: EasyAccuracy: 40.43%Submissions: 269K+Points: 2
Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.

Examples:

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat.
Input: s = "racecar"
Output: 'e'
Explanation: In the given string, 'e' is the only character in the string which does not repeat.
Input: s = "aabbccc"
Output: -1
Explanation: All the characters in the given string are repeating.
Constraints:
1 <= s.size() <= 105

Link: https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/
"""

#User function Template for python3
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        counter = {}

        for letter in s:
            if letter not in counter:
                counter[letter] = 0
            counter[letter] += 1
            
        for k, v in counter.items():
            if v == 1:
                return k
        else:
            return -1
