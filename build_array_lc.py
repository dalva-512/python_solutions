"""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

Example 1:
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
Example 2:

Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
The elements in nums are distinct.

Explanation with Examples
Let's break down the examples to see how the array ans is constructed.

Example 1:
Input: nums = [0, 2, 1, 5, 3, 4]
Output: ans = [0, 1, 2, 4, 5, 3]
Steps to construct ans:

ans[0] = nums[nums[0]] = nums[0] = 0
ans[1] = nums[nums[1]] = nums[2] = 1
ans[2] = nums[nums[2]] = nums[1] = 2
ans[3] = nums[nums[3]] = nums[5] = 4
ans[4] = nums[nums[4]] = nums[3] = 5
ans[5] = nums[nums[5]] = nums[4] = 3
So, the resulting array is ans = [0, 1, 2, 4, 5, 3].

Example 2:
Input: nums = [5, 0, 1, 2, 3, 4]
Output: ans = [4, 5, 0, 1, 2, 3]
Steps to construct ans:

ans[0] = nums[nums[0]] = nums[5] = 4
ans[1] = nums[nums[1]] = nums[0] = 5
ans[2] = nums[nums[2]] = nums[1] = 0
ans[3] = nums[nums[3]] = nums[2] = 1
ans[4] = nums[nums[4]] = nums[3] = 2
ans[5] = nums[nums[5]] = nums[4] = 3
So, the resulting array is ans = [4, 5, 0, 1, 2, 3].
"""
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans

# Example usage
nums1 = [0, 2, 1, 5, 3, 4]
sol = Solution()
result1 = sol.buildArray(nums1)
print(result1)  # Output: [0, 1, 2, 4, 5, 3]

nums2 = [5, 0, 1, 2, 3, 4]
result2 = sol.buildArray(nums2)
print(result2)  # Output: [4, 5, 0, 1, 2, 3]
