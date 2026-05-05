"""
20. Valid Parentheses

Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

# N is the length of s
# Time: O(N)
# Space: O(N) worst case
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in {'(','[','{'}:
                stack.append(char)
            elif char in {')',']','}'}:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return len(stack) == 0


def main():
    # Terminal takes the input as a string
    string = input("String of parentheses: ")
    is_valid = Solution().isValid(string)
    print(is_valid)

if __name__ == "__main__":
    main()