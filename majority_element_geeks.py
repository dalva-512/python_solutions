"""
Majority Element:
==================
Find the majority element in the array. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

Examples : 

Input : A[]={3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater than the half of the size of the array size. 

Input : A[] = {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element
Explanation: There is no element whose frequency is greater than the half of the size of the array size.

Link: https://www.geeksforgeeks.org/majority-element/
"""
def majority_element(arr: list):
    dct = dict()
    for i in arr:
        cnt = arr.count(arr[i])
        dct[i] = cnt
    print(dct)
    mid = int(len(arr)/2)
    for key, val in dct.items():
        if val > mid:
            return [key, val]
    return None

val = majority_element(arr)
if val is not None:
    print(f"The frequency of {val[0]} is {val[1]} which is greater than the half of the size of the array size.")
else:
    print("There is no element whose frequency is greater than the half of the size of the array size.")
