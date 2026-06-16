"""
34. Find First and Last Position of Element in Sorted Array

Difficulty: Medium
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

# N is the length of nums
# Binary Search
# Time: O(log N)
# Space: O(1)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def find_endpoint(left, right):
            lo, hi = 0, len(nums) - 1
            new_endpoint = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    new_endpoint = mid
                    if left:
                        hi = mid - 1  # search for left endpoint
                    if right:
                        lo = mid + 1  # search for right endpoint 
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return new_endpoint

        return [find_endpoint(left = True, right = False), find_endpoint(left = False, right = True)]
    

def main():
    # Terminal takes the input as a string
    numbers = [5,7,7,8,8,10]
    print("List: ", numbers)
    target = input("Target number are you interested in: ")
    bounds = Solution().searchRange(numbers,int(target))
    print('Bounds: ',bounds)

if __name__ == "__main__":
    main()