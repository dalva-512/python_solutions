"""
345. Reverse Vowels of a String
================================
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a', 'e', 'i', 'o', 'u']
        l = list(s)
        for i in range(len(l)):
            for j in range(i):
                if l[i] in vow and l[j] in vow:
                    l[i], l[j] = l[j], l[i]
        return ''.join(l)
