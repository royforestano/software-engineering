"""
33. Search in Rotated Sorted Array

Difficulty: Medium
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/


There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""

# N is the length of nums
# Time: O(log N)
# Space: O(1)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            # Left half is sorted, otherwise nums[mid] may be less than nums[left]
            if nums[left] <= nums[mid]:
                # Check where target is based on this
                if nums[left] <= target < nums[mid]:
                    right = mid - 1   # target in left sorted half
                else:
                    left = mid + 1   # target in right half
            # Right half is sorted (if left is not sorted, right half must be)
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # target in right sorted half
                else:
                    right = mid - 1   # target in left half
        return -1
        
