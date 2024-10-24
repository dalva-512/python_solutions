"""
Kth Smallest:
=============
Difficulty: MediumAccuracy: 35.17%Submissions: 650K+Points: 4
Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output:  7
Explanation: 3rd smallest element in the given array is 7.

Input: arr[] = [2, 3, 1, 20, 15], k = 4 
Output: 15
Explanation: 4th smallest element in the given array is 15.

Expected Time Complexity: O(n+(max_element) )
Expected Auxiliary Space: O(max_element)
Constraints:
1 <= arr.size <= 106
1<= arr[i] <= 106
1 <= k <= n
Link: https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1?page=1&company=Amazon&sortBy=submissions
"""
class Solution:
    def k_smallest(self, arr, k):
        if k > len(arr):
            return
        for i in range(len(arr) -1 , 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr[k - 1]
        
arr = [7, 10, 4, 3, 20, 15]
k = 3
sol = Solution()
ret_ar = sol.k_smallest(arr, k)
print(ret_ar)
