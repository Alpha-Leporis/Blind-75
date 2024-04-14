# Reverse Bits

# https://leetcode.com/problems/reverse-bits/description/

# https://www.youtube.com/watch?v=UcoN6UjAI64&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=14

'''

Reverse bits of a given 32 bits unsigned integer.

Note: Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Constraints:
    The input must be a binary string of length 32

Follow up: If this function is called many times, how would you optimize it?


'''


# solution:

# this function reverses the bits of the input integer n and returns the result.
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1  # Extract the i-th bit
            res = res | (bit << (31 - i))  # Set the i-th bit in the reversed number
        return res

# TC: O(1)
# SC: O(1)

'''

Here's a breakdown of how it works:

1. res = 0: Initialize a variable res to store the result of the reversed bits.

2. for i in range(32):: Iterate over each bit of the input integer n. Since we're dealing with a 32-bit integer, the loop runs from 0 to 31.

3. bit = (n >> i) & 1: Extract the i-th bit of n by right-shifting n by i positions and then performing a bitwise AND with 1. This operation isolates the i-th bit.

4. res = res | (bit << (31 - i)): Set the i-th bit of the result res to the value of bit, but shifted to its correct position in the reversed integer. This is achieved by left-shifting bit by (31 - i) positions and then performing a bitwise OR with res.

5. Finally, return res: Return the reversed 32-bit integer res.

'''

