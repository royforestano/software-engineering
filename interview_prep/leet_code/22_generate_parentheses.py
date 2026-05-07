"""
22. Generate Parentheses

Difficulty: Medium
Link: https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""

# N is the number of pairs of parentheses
# C is the possible number of combinations
# Time: O(C*2*N) ~ O(4^N/sqrt(N))
# Space: O(2*N)
class Solution(object):
    def generateParenthesis(self, n):
        result = []

        # l is the number of open parenthesis
        # r is the number of closed parenthesis
        def backtrack(seq, l, r):
            if len(seq) == 2 * n:
                result.append(seq)
                return
            if l < n:
                backtrack(seq + '(', l + 1, r)
            if r < l:
                backtrack(seq + ')', l, r + 1)

        backtrack('', 0, 0)
        return result