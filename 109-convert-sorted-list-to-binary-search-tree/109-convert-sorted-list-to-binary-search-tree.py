# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head:
            return head
        
        #左闭右开
        return self.helper(head, None)
    
    def helper(self, left, right):
        if left == right:
            return None
        
        slow = fast = left
        
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
            
        root = TreeNode(slow.val)
        root.left = self.helper(left, slow)
        root.right = self.helper(slow.next, right)
            
        return root
        
        