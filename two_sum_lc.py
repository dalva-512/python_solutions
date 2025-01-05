"""
Two Sum:
============
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1 = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    l1.append(i)
                    l1.append(j)
        return l1

#Solution 2:
def two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

op = two_sum(nums, target)
print(op)

#Solution 3:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums, target)
        val = []
        for i in nums:
            print(i)
            num = nums[1:]
            for j in num:
                if (i + j) == target:
                    in_i = nums.index(i)
                    in_j = nums.index(j)
                    val.append(in_i)
                    val.append(in_j)
                    print(val)
                    return val

#Solution 4: O(n)
def two_sum(nums, target):
    # Dictionary to store the indices of the numbers we have seen
    num_to_index = {}
    
    # Iterate through the array
    for index, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            # Return the indices of the two numbers
            return [num_to_index[complement], index]
        
        # Otherwise, add the current number and its index to the dictionary
        num_to_index[num] = index

