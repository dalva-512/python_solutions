"""
1929. Concatenation of Array
=============================
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
 

Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
"""
"""
Methods To Solve This Problem:
This post covers five different methods to concatenate an array with itself in Python. Each method is explained in a beginner-friendly way.

Using Loop and Append Method
Using Loop and Changing Element Value
Using Extend Method
Using + Operator
Using * Operator
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
            lst = nums + nums
            return lst
#OR:
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)  # Extend the list with itself. Cannot return it directly or assign it to a list. That would return None
        return nums

#OR:
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2  # Repeat the list twice
#OR:
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num)  # Add each element from nums
        for num in nums:
            result.append(num)  # Add each element again
        return result
