"""
Array Leaders:
==============
Difficulty: EasyAccuracy: 29.94%Submissions: 791K+Points: 2
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

Examples:

Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
Input: arr = [10, 4, 2, 4, 1]
Output: [10, 4, 4, 1]
Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side
Input: arr = [5, 10, 20, 40]
Output: [40]
Explanation: When an array is sorted in increasing order, only the rightmost element is leader.
Input: arr = [30, 10, 10, 5]
Output: [30, 10, 10, 5]
Explanation: When an array is sorted in non-increasing order, all elements are leaders.
Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 106

Link: https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620

"""
def find_leaders(arr):
    leaders = []
    max_so_far = float('-inf')  # Initialize to negative infinity

    # Traverse the array from right to left
    for i in reversed(range(len(arr))):
        if arr[i] >= max_so_far:
            leaders.append(arr[i])
            max_so_far = arr[i]

    # Reverse the leaders list to maintain the original order
    return leaders[::-1]

# Example Inputs
arr1 = [16, 17, 4, 3, 5, 2]
arr2 = [10, 4, 2, 4, 1]
arr3 = [5, 10, 20, 40]
arr4 = [30, 10, 10, 5]

# Outputs
print(find_leaders(arr1))  # Output: [17, 5, 2]
print(find_leaders(arr2))  # Output: [10, 4, 4, 1]
print(find_leaders(arr3))  # Output: [40]
print(find_leaders(arr4))  # Output: [30, 10, 10, 5]

"""
To solve this problem, the goal is to identify all the "leaders" in the array. A leader is an element that is greater than or equal to all elements to its right. The rightmost element is always a leader.

Approach
Iterate from Right to Left:

Start from the rightmost element, as it is always a leader.
Keep track of the maximum element encountered so far (max_so_far).
Compare each element with max_so_far. If it is greater than or equal to max_so_far, it is a leader, and you update max_so_far.
Time Complexity:

Since we traverse the array once (from right to left), the solution runs in O(n) time.
Space Complexity:

The solution requires O(k) space for storing the leaders in the result list, where k is the number of leaders. This is efficient compared to naive approaches.
Algorithm
Initialize an empty list leaders to store the leader elements.
Set max_so_far to negative infinity initially.
Traverse the array in reverse order:
If the current element is greater than or equal to max_so_far:
Add it to leaders.
Update max_so_far to the current element.
Since elements are added in reverse order, reverse the leaders list before returning it.

Explanation with Examples
Input: arr = [16, 17, 4, 3, 5, 2]

Start with max_so_far = -inf.
Traverse from right to left:
Compare 2 with -inf: Add 2 to leaders, update max_so_far = 2.
Compare 5 with 2: Add 5 to leaders, update max_so_far = 5.
Compare 3 with 5: Skip.
Compare 4 with 5: Skip.
Compare 17 with 5: Add 17 to leaders, update max_so_far = 17.
Compare 16 with 17: Skip.
Final leaders: [2, 5, 17] → Reverse to [17, 5, 2].
Input: arr = [10, 4, 2, 4, 1]

Leaders: [1, 4, 4, 10] → Reverse to [10, 4, 4, 1].
Input: arr = [5, 10, 20, 40]

Only 40 is a leader because the array is sorted in increasing order.
Input: arr = [30, 10, 10, 5]

All elements are leaders because the array is sorted in non-increasing order.
Constraints
Time Complexity: 
𝑂(𝑛) as we traverse the array once.
Space Complexity: 
𝑂(𝑘) where is the number of leaders (storage for the result).
This approach ensures efficiency and correctness for any input array that meets the constraints.
"""
