"""
24. Swap Nodes in Pairs

Difficulty: Medium
Link: https://leetcode.com/problems/swap-nodes-in-pairs/


Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation: Image

Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

"""

# N is the length of the list
# Time: O(N)
# Space: O(1)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = ListNode(0)
        new_head.next = head
        prev = new_head

        while prev.next and prev.next.next:
            first = prev.next        # first node to swap
            second = prev.next.next  # second node to swap

            first.next = second.next # point the first node one ahead of where it was pointing before, or one ahead of the second node
            second.next = first      # point the second node to teh first to swap
            prev.next = second       # previous node gets pointed to the new first ndoe after the swap

            prev = first             # advance prev to first node to swap, or the tail of the swapped pair

        return new_head.next