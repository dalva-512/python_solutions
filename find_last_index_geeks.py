"""
Find last index of a character in a string:
===========================================
Given a string str and a character x, find last index of x in str.

Examples : 
Input : str = "geeks", x = 'e'
Output : 2
Last index of 'e' in "geeks" is: 2 

Input : str = "Hello world!", x = 'o'
Output : 7
Last index of 'o' is: 7 
"""
def last_index(s: str, x: str) -> str:
    idx = s.rfind(x)
    return idx

print(f"Last index of {x} is :{last_index(s, x)}")
