"""
30. Substring with Concatenation of All Words

Difficulty: Hard
Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.

"""

# N is the length of s, L is the length of words, K is the length of one word
# Time: O(NxL)
# Space: O(K)
from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        window_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            curr_count = Counter()
            words_used = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    curr_count[word] += 1
                    words_used += 1

                    # Shrink window if this word appears too many times
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        words_used -= 1
                        left += word_len

                    if words_used == num_words:
                        result.append(left)
                        # Slide window forward by one word
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                else:
                    # Reset window
                    curr_count.clear()
                    words_used = 0
                    left = right + word_len

        return result