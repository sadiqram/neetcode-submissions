# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        tracker = set()
        if head is None or head.next is None:
            return False
        node = head
        
        while node.next:
            if node in tracker:
                return True
            tracker.add(node)
            node = node.next

        return False
        