"""
Cat and Hat:
=============
Difficulty: MediumAccuracy: 56.52%Submissions: 25K+Points: 4
You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.

Example 1:

Input:
str = catinahat
Output:
True
Explanation:
cat and hat both are present
1 number of times.
Example 2:

Input:
str = bazingaa
Output:
True
Explanation:
cat and hat both are present
0 number of times.
Link: https://www.geeksforgeeks.org/problems/cat-and-hat-python/1
"""
def check_cat_hat(str: str) -> bool:
    # Count occurrences of "cat" and "hat" in the string
    count_cat = str.count("cat")
    count_hat = str.count("hat")
    # Return True if the counts are equal, otherwise False
    return count_cat == count_hat
