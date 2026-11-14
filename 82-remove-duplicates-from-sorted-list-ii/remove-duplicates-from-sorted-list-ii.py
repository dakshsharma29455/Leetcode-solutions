# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # Dummy node handles cases where the head itself has duplicates and gets removed
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            # Check if current node is the start of a duplicate sequence
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Link prev to the node after the last duplicate
                prev.next = head.next
            else:
                # No duplicates, move prev forward
                prev = prev.next
            
            head = head.next
            
        return dummy.next
        