"""
18. 4Sum

Difficulty: Medium
Link: https://leetcode.com/problems/4sum/description/



Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

"""

# N is the length of nums, C is the number of possible unique combinations which exist
# Time: O(N^3)
# Space: O(4*C)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            # Each i is an anchor and the value at nums[i] only needs to be checked once
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Each j is a second anchor ahead of anchor i "" "" ""
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # i was zero, 0, at some point which means we already check all
                # values to the left of the cirrent i already, hence the n-3 in the loop
                # j+1 to n-1 will eventually "hit" into one another 
                left, right = j + 1, n - 1 

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result