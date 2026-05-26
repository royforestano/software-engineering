"""
28. Find the Index of the First Occurrence in a String

Difficulty: Easy
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""

# N is the length of haystack
# M is the length of needle
# Time: O(NxM) or O(N+M) for Knuth-Morris-Pratt (KMP) algorithm
# Space: O(M)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # # Time = O(NxM)
        # n, m = len(haystack), len(needle)
        # for i in range(n - m + 1):
        #     if haystack[i:i+m] == needle:
        #         return i
        # return -1

        # Time = O(N+M)
        # Knuth-Morris-Pratt (KMP) algorithm
        n, m = len(haystack), len(needle)

        # Build failure function for NEEDLE
        fail = [0] * m
        j = 0
        for i in range(1, m):
            # If no match after found a match, revert back to 
            # previous characters last known set of matches
            while j > 0 and needle[i] != needle[j]:
                j = fail[j-1]
            # When an already seen charcter shows up again, go to the next index
            # since there will be some checking that validates the first set of characters match
            if needle[i] == needle[j]:
                j += 1
            fail[i] = j

        # Search
        j = 0
        for i in range(n):
            # If no match after found a match, revert back to previous characters last known set of matches
            while j > 0 and haystack[i] != needle[j]:
                j = fail[j-1]
            # If match, keep going
            if haystack[i] == needle[j]:
                j += 1
            # If j counted to length of needle, return index
            if j == m:
                return i - m + 1
        return -1