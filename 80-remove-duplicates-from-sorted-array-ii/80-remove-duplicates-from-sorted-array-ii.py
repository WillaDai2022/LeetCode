class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        #p指向第一个无效位置
        p = 2
                
        for i in range(2, len(nums)):
            if nums[i] != nums[p-2]:
                nums[p] = nums[i]
                p += 1
                
        return p
                    