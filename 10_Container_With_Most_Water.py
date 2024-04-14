# Container With Most Water

# https://leetcode.com/problems/container-with-most-water/description/

# https://www.youtube.com/watch?v=UuiTKBwPgAo&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=10

'''

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

'''

# solution: sliding window --> Two pointers


# Brute force solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for l in range(len(height)):
            for r in range(l+1,len(height)):
                area = (r - l) * min(height[l], height[r])   # Area of rectangle --> (width * height)
                res = max(res, area)
        return res


# TC: O(n^2)
# SC: O(1)


# optimized solution --> Two pointers

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        while(l < r):
            area = (r - l) * min(height[l], height[r])  # Area of rectangle --> (width * height)
            res = max(res, area)
            if height[l] < height[r]:
                l +=1
            elif height[l] > height[r]:
                r -= 1
            else: # height[l] == height[r] --> then we increment our left pointer or decrement our right pointer
                r -= 1
    
        return ans


# TC: O(n)
# SC: O(1)