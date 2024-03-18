"""
Triplet Sum in Array (3sum):
==============================
Find a triplet that sums to a given value
Given an array arr[] of size n and an integer X. Find if there’s a triplet in the array which sums up to the given integer X.

Examples: 
Input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
Output: 12, 3, 9 
Explanation: There is a triplet (12, 3 and 9) present 
in the array whose sum is 24. 

Input: array = {1, 2, 3, 4, 5}, sum = 9 
Output: 5, 3, 1 
Explanation: There is a triplet (5, 3 and 1) present 
in the array whose sum is 9.

"""
def triplet_sum(arr, sm):
    ln = len(arr)
    for i in range(len(arr) - 2):
        for j in range(1, len(arr) -1):   # Here the 3 for loop needs to be used insted of j = i + 1 and k = j + 1 because it needs to traverse accross the array and not only the adjacent numbers.
            for k in range(2, len(arr)):
                addtn = arr[i] + arr[j] + arr[k]
                if addtn == sm:
                    return [arr[i], arr[j], arr[k]]
    else:
        return -1

trip_sum = triplet_sum(arr, sm)
print(f"The Triplet sum is: {trip_sum}")
