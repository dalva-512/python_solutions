"""
Consecutive Characters:
=====================
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
Input: s = "counttheconsecutive"
Output: 2

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters.:
"""
def maxPower(s: str) -> int:
    if not s:
        return 0
    
    max_power = 1  # Minimum power is always 1 as every character has power at least 1
    current_power = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_power += 1
        else:
            current_power = 1
        
        max_power = max(max_power, current_power)
    
    return max_power

s = "leetcode"
op = maxPower(s)
print(op)

"""
We initialize max_power and current_power to 1, as every character has at least a power of 1.
We iterate over the string, checking if the current character is the same as the previous one. If it is, we increment current_power, else we reset it to 1.
We update max_power whenever we encounter a new maximum power. Finally, we return max_power.
"""
