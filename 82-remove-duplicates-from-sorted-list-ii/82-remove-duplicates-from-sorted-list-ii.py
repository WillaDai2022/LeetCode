# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        curr = dummy
        
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                value = curr.next.val
                while curr.next and curr.next.val == value:
                    curr.next = curr.next.next
            else:
                curr = curr.next
                
        return dummy.next
            
            