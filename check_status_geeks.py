"""
Check the status - Python
Difficulty: EasyAccuracy: 20.06%Submissions: 107K+Points: 2
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return false.

Geeksforgeeks: https://www.geeksforgeeks.org/problems/check-the-status/1
"""
def check_status(a, b, flag):
    if (a >= 0) != (b >= 0) and not flag:
        return True
    if a < 0 and b < 0 and flag:
        return True
    return False

"""
Explanation:
The condition (a >= 0) != (b >= 0) ensures that one of a or b is non-negative, but not both.
This is equivalent to an XOR operation for checking opposite conditions.
The second condition checks if both a and b are negative, and flag is true.
If neither condition is satisfied, the function returns False.
"""
