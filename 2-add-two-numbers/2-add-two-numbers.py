# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        carry = 0
        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
                
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
                
            sum = carry + num1 + num2
            curr_val = sum % 10
            carry = sum // 10
            
            curr.next = ListNode(curr_val)
            curr = curr.next
            
        return dummy.next
            