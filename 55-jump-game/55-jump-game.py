class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #greedy set goal as the end of the list, if the previous number
        #can reach the goal, remove goal to the previous index
        
        goal = len(nums)-1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0