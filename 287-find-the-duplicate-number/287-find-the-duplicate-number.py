class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #本题可以看作是一个环形链表
        #[1,2,4,2,2,] 索引为0，1，2，3，4
        #nums[0]指向2，第一个节点为nums[0], 则下一个节点为nums[nums[0]]即为2
        #0 -> 1 -> 2 -> 4 -> -> 4 ->4...
        #快慢指针找到相遇点，一定在环内
        slow, fast = 0,0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        #从起点开始到环形起点的距离等于当前快慢指针相遇之处走至环形起点的距离    
        slow2 = 0
        
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
            
        return slow