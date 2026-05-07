"""
23. Merge k Sorted Lists

Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

# N is the total number of elements across all lists to merge
# h is size of the heap
# Each time an element is added to a min-heap, takes O(log h) time
# Time: O(N*log h) # have to put all elements in the heap
# Space: O(h) 
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq 
class Solution(object):
    def mergeKLists(self, lists):
        merged = ListNode(0)
        current = merged
        heap = [] 

        # Push the head of each non-empty list onto the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node)) # min-heap by default

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return merged.next