"""
32. Longest Valid Parentheses

Difficulty: Hard
Link: https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.


"""
# Approach 1: Two-pass counting "(" vs. ")"
# Time: O(N)
# Space: O(1)
class Solution(object):
    def longestValidParentheses(self, s):
        longest = 0

        # Left to right
        left = right = 0
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                longest = max(longest, 2 * right)
            elif right > left:
                left = right = 0

        # Right to left
        left = right = 0
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                longest = max(longest, 2 * left)
            elif left > right:
                left = right = 0

        return longest



# Approach 2: Stack storing location of last fail point
# Time: O(N)
# Space: O(N)
class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]  # base index sentinel
        longest = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # new base: this unmatched ')' 
                else:
                    longest = max(longest, i - stack[-1])

        return longest