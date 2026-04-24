"""
10. Regular Expression Matching

Difficulty: Hard
Link: https://leetcode.com/problems/regular-expression-matching/description/


Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).


Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.



"""

# N is teh text length, M is the pattern length
# Time: O(N*M)
# Space: O(N*M)
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text) # if finish going through the pattern, also want to finish the text
                else:
                    # check to make sure there is more text
                    # see if the j-th pattern character is the i-th text character is if it is the "any element" delimiter "."
                    first_match = i < len(text) and pattern[j] in {text[i], "."} 
                    # make sure there is more pattern and 
                    # check if it should match the previous character
                    if j + 1 < len(pattern) and pattern[j + 1] == "*":
                        # First: Check if you reach the end or ( I am not sure)
                        # Second: make sure pattern[j] is text[i] and check if pattern [j]
                        # is text[i+1] indicating "*" admits True
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        # Continue along until a special character shows up
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
