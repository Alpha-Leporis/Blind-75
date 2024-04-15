# Longest Increasing Subsequence

# https://www.youtube.com/watch?v=cjWnW0hdF1Y&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=17

# https://leetcode.com/problems/longest-increasing-subsequence/description/

'''

Given an integer array nums, return the length of the longest strictly increasing subsequence

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


'''

# solution: DP Bottom-up

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

# TC: O(n^2)
# SC: O(1) 

# optimized solution: Binary search

# https://www.youtube.com/watch?v=_xY8VTllU8E

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)  # size same as length of nums array
        size = 0 # keep track of the longest increasing subsequence
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

# TC: O(nlogn)
# SC: O(1) 