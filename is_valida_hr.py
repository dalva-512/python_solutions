"""
Sherlock and the Valid String:
============================
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

Example
s = abc
This is a valid string because frequencies are .{'a': 1, 'b': 1, 'c': 1}

s = "aabcd"
This is a valid string because we can remove one of a and have 1 of each character in the remaining string. {'a': 2, 'b': 1, 'c': 1, 'd': 1}

s = "abccc"
This string is not valid as we can only remove 1 occurrence of c . That leaves character frequencies of {'a': 1, 'b': 1, 'c': 2}.

s = "aabbc" - Invalid

Function Description

Complete the isValid function in the editor below.

isValid has the following parameter(s):

string s: a string
Returns

string: either YES or NO
Input Format

A single string .

Constraints

Each character 
Sample Input 0

aabbcd
Sample Output 0

NO
Explanation 0

Given , we would need to remove two characters, both c and d  aabb or a and b  abcd, to make it valid. We are limited to removing only one character, so  is invalid.

Sample Input 1

aabbccddeefghi
Sample Output 1

NO
Explanation 1

Frequency counts for the letters are as follows:

{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

There are two ways to make the valid string:

Remove  characters with a frequency of : .
Remove  characters of frequency : .
Neither of these is an option.

Sample Input 2

abcdefghhgfedecba
Sample Output 2

YES
Explanation 2

All characters occur twice except for  which occurs  times. We can delete one instance of  to have a valid string.

Language
Python 3
More
141516171819202122232413111291067823451
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
…    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()



Line: 48 Col: 1

Test against custom input
7/20 test cases failed :(

Ask your friends for help:Share on FacebookShare on TwitterShare on LinkedIn

Test case 4

Test case 5

Test case 7

Test case 13

Test case 14

Test case 16

Test case 18

Test case 0

Test case 1

Test case 2

Test case 3

Test case 6

Test case 8

Test case 9

Test case 10

Test case 11

Test case 12

Test case 15

Test case 17

Test case 19
Compiler Message
Wrong Answer
Hidden Test Case
Unlock this testcase for 5 hackos.

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    cnt = 0
    dup = False
    dct = dict()
    for i in s:
        cnt = s.count(i)
        dct[i] = cnt
    for val in dct.values():
        if val >= 2:
            cnt += 1
            if cnt > 2:
                dup = False
                break
        else:
            dup = True
            continue
    if dup:
        return "YES"
    else:
        return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
