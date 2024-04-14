# Counting Bits - Dynamic Programming

# https://www.youtube.com/watch?v=RyBM56RIWrM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=12

# https://leetcode.com/problems/counting-bits/description/


'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:
    0 <= n <= 105

Follow up:
    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

'''

# Solution: DP
'''
when we divide any integer by 2 (integer division) the time complexity will be O(log₂n) --> O(log n)
and we are doing with the bunch of integers so the overall time complexity will be O(n log n)
now there is some repeted work which we can eleminate we can do this by easylly recorgnize by 
(bit mappings) binary representation of integers

0 = 0000 --> 0
1 = 0001 --> 1 + dp[n-1]     -->>  dp[n-1]  --> 1-1 --> 0 --> 0000
2 = 0010 --> 1 + dp[n-2]
3 = 0011 --> 1 + dp[n-2]
4 = 0100 --> 1 + dp[n-4]
5 = 0101 --> 1 + dp[n-4]
6 = 0110 --> 2 + dp[n-4]
7 = 0111 --> 3 + dp[n-4]
8 = 1000 --> 1 + dp[n-8]

'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1 # the highest power of 2 so far
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp

# TC: O(1)
# SC: O(1)