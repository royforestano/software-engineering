"""
25. Reverse Nodes in k-Group

Difficulty: Hard
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?

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
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        new_head = ListNode(0)
        new_head.next = head
        prev = new_head

        while True:
            # Step 1: check if k nodes remain
            check = prev
            for _ in range(k):
                check = check.next
                if not check:
                    return new_head.next

            # Step 2: identify the k nodes
            tail = prev.next      # first node will be at the back after reversal
            current = prev.next   # current node is the one we adjust its next value to be
            prev_node = None      # prev_node becomes current.next (reverse nodes)

            # Step 3: reverse k nodes
            for _ in range(k):
                nxt = current.next       # save the next value in the current k term sequence before modifying
                current.next = prev_node # change the pointer of the current node you are looking at
                                         # to the previous node you were modifying (prev_node/curr tail)
                prev_node = current      # the previous node now becomes the current one
                current = nxt            # current one becomes the next one we saved

                                         # prev_node is now the new head of this group
                                         # tail is still the tail of group

            # Step 4: reconnect 
            prev.next = prev_node   # connect previous group to new head
            tail.next = current     # connect new tail to remainder of sequence
            prev = tail             # advance prev to tail of reversed group

        return new_head.next