"""
16. 3Sum Closest

Difficulty: Medium
Link: https://leetcode.com/problems/3sum-closest/description/


Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

"""


# N is the length of nums
# Time: O(N^2)
# Space: O(1)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums)<3:
            return 0
        
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]  # real initial value

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum == target:
                    return curr_sum          # can't get closer than exact
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum