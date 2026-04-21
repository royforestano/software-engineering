"""
5. Longest Palindromic Substring

Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

# N is the length of the string
# L is the length of the longest palindromic substring
# Time: O(N^2)
# Space: O(L)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        def expand(left, right):
            # Expand outward while characters match and indices are valid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right have gone one step too far, so slice back
            return s[left + 1 : right]

        longest = ""
        for i in range(len(s)):
            odd  = expand(i, i)       # e.g. center = "b" in "aba"
            even = expand(i, i + 1)   # e.g. center = "bb" in "abba"

            if len(odd)  > len(longest): longest = odd
            if len(even) > len(longest): longest = even

        return longest