class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_start(nums, target)
        right = self.find_end(nums, target)
        return [left, right]
       
    def find_start(self,nums, target):
        left, right = 0, len(nums)-1
        index = -1

        while left <= right:
            middle = (left + right)//2
            if nums[middle] == target:
                index = middle
                
            if nums[middle] >= target:
                right = middle -1
            else:
                left = middle + 1
        return index

    def find_end(self,nums, target):
        left, right = 0, len(nums)-1
        index = -1

        while left <= right:
            middle = (left + right)//2
            if nums[middle] == target:
                index = middle

            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1

        return index


       