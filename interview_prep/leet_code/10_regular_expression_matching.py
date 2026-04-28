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

# N is the s length, M is the p length
# Time: O(N*M)
# Space: O(N*M)
class Solution(object):
    def isMatch(self, s,p):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s) # if finish going through the p, also want to finish the s
                else:
                    # check to make sure there is more s
                    # see if the j-th p character is the i-th s character is if it is the "any element" delimiter "."
                    first_match = i < len(s) and p[j] in {s[i], "."} 
                    # make sure there is more p and 
                    # check if it should match the previous character
                    if j + 1 < len(p) and p[j + 1] == "*":
                        # First: Check if you reach the end or a "letter*" combination which is a single character
                        # Second: make sure p[j] is s[i] and check if p [j]
                        # is s[i+1] indicating "*" admits True
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        # Continue along until a special character shows up
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
