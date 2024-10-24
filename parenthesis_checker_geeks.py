"""
Parenthesis Checker:
=====================
You are given a string s representing an expression containing various types of brackets: {}, (), and []. Your task is to determine whether the brackets in the expression are balanced. A balanced expression is one where every opening bracket has a corresponding closing bracket in the correct order.

Examples :

Input: s = "{([])}"
Output: true
Explanation: 
 
Same colored brackets can form balanced pairs, with 0 number of unbalanced bracket.
Input: s = "()"
Output: true
Explanation:
  
Same bracket can form balanced pairs,and here only 1 type of bracket is present and in balanced way.
Input: s = "([]"
Output: false
Explanation: 
 
Here square bracket is balanced but the small bracket is not balanced and Hence , the output will be unbalanced.
Constraints:
1 ≤ s.size() ≤ 106
s[i] ∈ {'{', '}', '(', ')', '[', ']'}
"""
class Solution:
    para = {"{": "}", "(":")", "[":"]"}
    def parenthesis_check(self, arr):
        for i in arr:
            for key, val in self.para.items():
                if key == i and val not in arr:
                    return False
        else:
            return True
        
s = "([]"
sol = Solution()
ret_ar = sol.parenthesis_check(s)
print(ret_ar)
