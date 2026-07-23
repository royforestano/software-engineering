'''
38. Count and Say

Difficulty: Medium
Link: https://leetcode.com/problems/count-and-say/


The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing each maximal group of consecutive identical characters with the concatenation of the length of the group followed by the character itself. For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15", and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

 

Constraints:

1 <= n <= 30

'''

# DP or Recursion
# N is the length of the count and say sequence of interest
# L is the longest RLE formed
# Time: O(N*L) (max) ~ O(N*2^N) upper bound since it nearly doubles each time
# Space: O(L)

# Approach 1: DP (iterative and more intuitive)
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def get_rle(c):
            i = 0
            rle = ''
            while i<len(c):
                cur_char = c[i]
                count_char = 0
                while i<len(c) and cur_char==c[i]:
                    count_char+=1
                    i+=1
                rle+=str(count_char)+cur_char
            return rle

        cns = '1'
        for i in range(n-1):
            cns = get_rle(cns)

        return cns

# Approach 2: Recursive (simpler) but takes more space
# Space: O(N*L) due to the call stack
class Solution(object):
    def countAndSay(self, n):
        def get_rle(c):
            i = 0
            rle = ''
            while i < len(c):
                cur_char = c[i]
                count_char = 0
                while i < len(c) and cur_char == c[i]:
                    count_char += 1
                    i += 1
                rle += str(count_char)
                rle += cur_char
            return rle

        # Base case
        if n == 1:
            return '1'

        # Recursive case: RLE of the previous term
        return get_rle(self.countAndSay(n - 1))


def main():
    # Terminal takes the input as a string
    n = input("Integer: ")
    cns = Solution().countAndSay(int(n))
    print('N-th element of Count and Say Sequence: ',cns)

if __name__ == "__main__":
    main()