# Maximum Product Subarray - Dynamic Programming

# https://www.youtube.com/watch?v=lXVy6YWFcRM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=6

# 

'''

Given an integer array nums, find the
subarray
with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''
# solution: dynamic programming

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        CurrMin, CurrMax = 1, 1
        for n in nums:
            if n == 0: # Edge case (ZERO): [1,2,-4,0,8]
                CurrMin, CurrMax = 1, 1
                continue
            tmp = CurrMax * n
            CurrMax = max(n * CurrMax, n * CurrMin, n) # [-1,8]
            CurrMin = min(tmp, n * CurrMin, n) # [-1,-8]
            result = max(result,CurrMax)
        return result

# TC: O(n)
# SC: O(1)