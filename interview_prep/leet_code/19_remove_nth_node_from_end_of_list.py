
"""
19. Remove Nth Node From End of List

Difficulty: Medium
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


"""
# N is the length of the linked list
# Time: O(N)
# Space: O(1)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        new_head = ListNode(0)
        new_head.next = head
        fast = new_head
        slow = new_head

        # advance fast n+1 steps so the gap between fast and slow is n
        for _ in range(n + 1):
            fast = fast.next

        # move both until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # slow is now at the node just before the one to remove
        slow.next = slow.next.next

        return new_head.next