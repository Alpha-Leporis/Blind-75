# Number of 1 Bits

# https://leetcode.com/problems/number-of-1-bits/description/

# https://www.youtube.com/watch?v=5Km3utixwZs&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=11

'''

Write a function that takes the binary representation of a positive integer and returns the number of
set bits it has (also known as the Hamming weight).


Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
    1 <= n <= 231 - 1

Follow up: If this function is called many times, how would you optimize it?

'''

# solution: bitwise
'''
we can take n and modding it with 2 --> 'n % 2'
modding is basically we take 1001 and divide it by 2 (n % 2) --> if there is 1 then it will return 1 else return 0
now we are able to detect if the first bit is 1 or 0, but what if we have to look at the next bit
the easyest wayto take all rest of the bits and shift them right by 1 (n >> 1),     we can also do the same by integer division (n / 2)

1011 % 2 = 1 # when output is 1 increment the result by 1.
1011 >> 1  # shift right by 1 and we'll get 101
res+=1

101 % 2 = 1  # when output is 1 increment the result by 1. 
101 >> 1 
res+=1

10 % 2 = 0 # when output is 0  do not increment the result.
10 >> 1

1 % 2 = 1 # when output is 1 increment the result by 1.
1 >> 1
res+=1

'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2  # 
            n = n >> 1
        return res

# TC: O(32) --> O(1)
# SC: O(1)

# Downside of this solution is that it has to look every bit even the one's that arent 1's
# It will be convinent if we look at the bits that are 1's.
# so that our algorithem only runs when the the bit is 1.


# optimized solution: now what we can do is we can use logicalAnd operator on n in while loop

'''
when we doing (n-1) we are actually getting rid of a bit from 'n', and we are counting that bit by'res+=1' 
and we are logicallyAnd'ED together with itself 'n & (n-1)' we are basically removing that 1 bit

n = n & (n-1)  -->    10000001
                    & 10000000
                    ----------
                      10000000
                    ----------
res += 1

do the same and get rid of the 1 bit

n = n & (n-1)  -->    10000000
                    & 01111111
                    ----------
                      00000000
                    ----------
res += 1

now we are done with our entire loop, now we have all zero's and we have incremented our res by 2
so our result is 2

res = 2

basically we are skipping all the zeros in between n
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n-1) # or n &= (n-1)
            res += 1
        return res


# TC: O(1)
# SC: O(1)



