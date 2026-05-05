"""
21. Merge Two Sorted Lists

Difficultuy: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/description/


You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

# L1 is the length of list 1
# L2 is the length of list 2
# Time: O(L1+L2)
# Space: O(1)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        merged_list = ListNode(0)
        current = merged_list
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val<=p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        current.next = p1 if p1 else p2
        return merged_list.next