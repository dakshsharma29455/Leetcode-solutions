# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the linked list and locate the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # Step 2: Handle cases where k >= length
        k = k % length
        if k == 0:
            return head
            
        # Step 3: Connect tail to head to form a circular list
        tail.next = head
        
        # Step 4: Find the new tail at position (length - k - 1)
        # and the new head at position (length - k)
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        
        # Step 5: Break the circular connection
        new_tail.next = None
        
        return new_head
        