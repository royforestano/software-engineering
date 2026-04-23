"""
7. Reverse Integer

Difficulty: Medium
Link: https://leetcode.com/problems/reverse-integer/description/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

# N is the number of digits in x
# Time: O(N)
# Space: O(N)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        result = sign * int(reversed_str)
        if result < -(2**31) or result > (2**31 - 1):
            return 0
        return result