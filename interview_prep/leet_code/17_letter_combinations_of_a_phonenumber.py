"""
17. Letter Combinations of a Phone Number

Difficulty: Medium
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""

# L is the length of digits
# Time: ~O(L*4^L), 4^L is about the maximum number of combinations each of length L
# Space: O(L*4^L) store all combinations as strings of length L
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits_to_letter = {'2':['a','b','c'],
                         '3':['d','e','f'],
                         '4':['g','h','i'],
                         '5':['j','k','l'],
                         '6':['m','n','o'],
                         '7':['p','q','r','s'],
                         '8':['t','u','v'],
                         '9':['w','x','y','z']}
        if not digits:
            return []
        
        poss_comb = []
        for digit in digits:
            curr_comb = []
            for letter in digits_to_letter[digit]:
                if len(poss_comb)>0:
                    for i in range(len(poss_comb)):
                        curr_comb.append(poss_comb[i]+letter)
                else:
                    curr_comb.append(letter)
            poss_comb = curr_comb

        return poss_comb