"""
4. Median of Two Sorted Arrays

Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/


Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


"""

# Binary search finding the right partition
# N is the length of nums1 and M is the length of nums2
# Time: O(log[min(N,M)])
# Space: O(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        half = (n+m) // 2
        lo = 0
        hi = n
        
        # maintains correct# elements, i+j = half_length
        while lo <= hi:
            i = (lo + hi) // 2   # partition in nums1, we want to find i
            j = half - i          # partition in nums2, automatically defined by i

            # Boundary Conditions
            nums1_left  = nums1[i-1] if i > 0 else float('-inf')
            nums1_right = nums1[i]   if i < n else float('inf')
            nums2_left  = nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j]   if j < m else float('inf')

            # We get that all elements to the left of nums1[i-1] in nums1 are less than that element
            # We have to check that they are also less than the ones to the right of j-1 in nums2

            # We get that all elements to the left of nums2[j-1] in nums2 are less than that element
            # We have to check that they are also less than the ones to the right of i-1 in nums1
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Found correct partition
                if (n+m) % 2 == 1:
                    return float(min(nums1_right, nums2_right))
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            elif nums1_left > nums2_right:
                hi = i - 1   # too far right in nums1, get smaller in nums1
            else:
                lo = i + 1   # too far left in nums1, get bigger in nums2