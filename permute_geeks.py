"""
Permutations of given String:
============================
Given a string S, the task is to write a program to print all permutations of a given string. 

A permutation also called an “arrangement number” or “order,” is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length N has N! permutations. 

Examples:

Input: S = “ABC”
Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”

Link: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
"""
# Python3 program to print all permutations with 
# duplicates allowed 
# Print permutations of a given string using backtracking:
  
  
def toString(List): 
    return ''.join(List) 
  
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
  
  
def permute(a, l, r): 
    if l == r: 
        print(toString(a)) 
    else: 
        for i in range(l, r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]  # backtrack 
  
  
# Driver code 
string = "ABC"
n = len(string) 
a = list(string) 
  
# Function call 
permute(a, 0, n) 
