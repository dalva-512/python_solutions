"""
3 Sum – Pythagorean Triplet in an array
Last Updated : 15 Oct, 2024
Given an array of positive integers, the task is to determine if a Pythagorean triplet exists in the given array. A triplet {a, b, c} is considered a Pythagorean triplet if it satisfies the condition a2 + b2 = c2.

Example:

Input: arr[] = {3, 1, 4, 6, 5} 
Output: True
Explanation: The array contains a Pythagorean triplet {3, 4, 5}.


Input: arr[] = {10, 4, 6, 12, 5} 
Output: False 
Explanation: There is no Pythagorean triplet. 
Link: https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
"""
class Solution:
    def triplets(self, arr) -> int:
        for i in range(len(arr) - 2):
            for j in range(1, len(arr) - 1):
                for k in range(2, len(arr)):
                    a = arr[i] ** 2
                    b = arr[j] ** 2
                    c = arr[k] ** 2
                    if a + b == c:
                        return True
        return False

# OR:
def pythagoreanTriplet(arr):
    n = len(arr)

    # Exploring all possible triplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                # Calculate square of array elements
                x = arr[i] ** 2
                y = arr[j] ** 2
                z = arr[k] ** 2

                # If these integers form Pythagorean triplet then
                # return true
                if x == y + z or y == x + z or z == x + y:
                    return True

    return False

arr = [3, 1, 4, 6, 5]

arr = [10, 4, 6, 12, 5]
sol = Solution()
val = sol.triplets(arr)
print(val)
