# Climbing Stairs


# https://leetcode.com/problems/climbing-stairs/description/

# https://www.youtube.com/watch?v=Y0lT9Fck7qI&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=15

'''

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
    1 <= n <= 45

'''

# solution: Brute force --> Decision Tree DFS --> TC: O(2^n)




# solution: DP (Bottom up)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        two_back = 1
        one_back = 2
        for i in range(2,n):
            curr = two_back + one_back
            two_back = one_back
            one_back = curr
        return curr


# TC: O(1)
# SC: O(1)