"""
6. Zigzag Conversion

Difficulty: Medium
Link: https://leetcode.com/problems/zigzag-conversion/


The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

# N is the length of the string s
# Time: O(N) 
# Space: O(N)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # Traverse in pattern it is saved in, but modify/add to the order (rows in
        # this case) we expect
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        row, direction = 0, 1

        for char in s:
            rows[row] += char
            if row == 0:
                direction = 1        # hit top, go down
            elif row == numRows - 1:
                direction = -1       # hit bottom, go up
            row += direction

        return ''.join(rows)