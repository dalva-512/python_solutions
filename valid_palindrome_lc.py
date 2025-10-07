"""
Valid Palindrome:
===================
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s3 = re.sub("\W+", "", s1)
        s2 = s3[::-1]
        if s3 == s2:
            return True
        else:
            return False
# Sol2:
def palindrome(s):
    s1 = ''.join(s.split())
    print(s1)
    if s1 == s1[::-1]:
        return True
    else:
        return False
