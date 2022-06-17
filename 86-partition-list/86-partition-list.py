# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        small_dummy = ListNode()
        big_dummy = ListNode()
        curr_small = small_dummy
        curr_big = big_dummy
        
        curr = head
        
        while curr:
            if curr.val < x:
                curr_small.next = curr
                curr_small = curr_small.next
            else:
                curr_big.next = curr
                curr_big = curr_big.next
                
            curr = curr.next
            
        curr_small.next = big_dummy.next
        curr_big.next = None
        
        return small_dummy.next