# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        
        prev_left, curr_left = dummy, head
        
        #reach node at position left and left-1
        for i in range(left - 1):
            prev_left = prev_left.next
            curr_left = curr_left.next
        
        #reverse the list from left to right
        prev = None
        for i in range(right - left + 1):
            curr_next = curr_left.next
            curr_left.next = prev
            prev = curr_left
            curr_left = curr_next
            
        prev_left.next.next = curr_left
        prev_left.next = prev
        
        return dummy.next