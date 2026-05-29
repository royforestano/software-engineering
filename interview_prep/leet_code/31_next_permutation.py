"""
31. Next Permutation

Difficulty: Medium
Link: https://leetcode.com/problems/next-permutation/description/


A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100


"""
# N is the length of nums
# Time: O(N)
# Space: O(1)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # In a gist, starting from the back (i) "climb the ladder" until the ladder goes down instead of up. nums[i]<nums[i+1]
        # This is the "inflection point." Go "climb the ladder again" (j) and and see if any values before (to the right of) the 
        # "inflection point" are geater than the value at nums[i]. nums[j] will either be nums[i+1], if everything
        # to the right of nums[i+1] is less than or equal to nums[i], or some other value on "the ladder" nums[j] which is
        # larger than nums[i] (minimum larger element) but smaller than nums[i+1], otherwise that would have been an inflection point.
        # Swap nums[i] with nums[j] to form a "greater sequence," then reverse the end to form the minimum next greatest sequence.
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            # Step 2: find rightmost j where nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: swap
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse from i+1 to end
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# The problem description does a poor job, in my opinion, of describing the rules
# in order to develop a sound solution.
# Lexicographically in this context refers to the string representation of a value and its digits
# For example, '10' would come after '2' because the number 1<2, however, the solution they anticipate does 
# not seem to follow this definition as it uses the numerical entries.

# My initial approach to quantify it mathematically
# Use a cumulative difference
# A lexicographically greater sequence will have a cum_diff 
# with "more" positive values on the left and "more" negative values on the right
# The total sum should be greater than or equal to the previous sequence
# e.g. [2,3,1] to [3,1,2]. At first you might think the solutiuon is [3,2,1]
# but check the differences of each [-1,2] with a total of +1 for [2,3,1]
# and [2,-1] with a total of +1 for for [3,1,2]
# and [1,1] with a total of +2 for [3,2,1] which is clearly the greatest sequence possible
# [3,1,2] ends up being the next permutation because [2,-1] is better than [-1,2] 
# and the sum of differences remains the same.

# def cum_diff(n):
#     return [int(str(n[i])[0])-int(str(n[i+1])[0]) for i in range(len(n)-1)]
# if len(nums)>1:
#     cum_difference = cum_diff(nums)
#     cum_diff_total = sum(cum_difference)

#     for i in range(len(nums)):