# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            temp = second.next
            second.next = prev
            prev, second = second, temp
            
        first,second = head, prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            
        