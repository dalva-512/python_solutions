"""
Check whether two Strings are anagram of each other:
=====================================================
Given two strings. The task is to check whether the given strings are anagrams of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.

Examples:

Input: str1 = “listen”  str2 = “silent”
Output: “Anagram”
Explanation: All characters of “listen” and “silent” are the same.

Input: str1 = “gram”  str2 = “arm”
Output: “Not Anagram”
"""
#Solution 1:
class Solution:
    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        a = a.lower()
        b = b.lower()
        if sorted(a) == sorted(b):
            return True
        else:
            return False
 
# {
#  Driver Code Starts
 
if __name__ == '__main__':
    a = "gram"
    b = "arm"
    if(Solution().isAnagram(a, b)):
      print("The two strings are anagram of each other")
    else:
      print("The two strings are not anagram of each other")
# } Driver Code Ends

#Solution 2:
def anagram(str1, str2):
    for i in range(len(str1)):
        if str1[i] not in str2:
            return False
        else:
            continue
    return True
  
op = anagram(str1, str2)
if op:
    print("Anagram")
else:
    print("Not Anagram")
