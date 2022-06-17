# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        
        curr = dummy
       
        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next
            
            node1.next = node2.next
            node2.next = node1
            curr.next = node2
            curr = curr.next.next
            
        return dummy.next
        
        