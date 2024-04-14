# Sum of Two Integers

# https://www.youtube.com/watch?v=_pUidg9gQyA

# https://leetcode.com/problems/sum-of-two-integers/description/

'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:

    -1000 <= a, b <= 1000

'''

# solution --> bitwise

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b!= 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        return a

# TC: O(1)
# SC: O(1)

# above code gives TLE Because Python uses lot of bits. the solution of this problem is to use bitshortner
        
class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitShortner = 0xffffffff
        while (b & bitShortner) > 0: # now 'b' chould be nagative that's why changed '!=' to '>'
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        # In the end we have to return a & with bitShortner only if b > 0 else return a
        return (a & bitShortner) if b > 0 else a

# TC: O(1)
# SC: O(1)