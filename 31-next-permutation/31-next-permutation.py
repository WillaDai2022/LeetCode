class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i):
            left = i
            right = len(nums) -1
            
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        n = len(nums)
        
        #find the first number in decending order
        index1 = n -2
        while index1 >= 0:
            if nums[index1] >= nums[index1 + 1]:
                index1 -= 1
            else:
                break

        #if the whole list is decending order, reverse the whole list
        if index1 == -1:
            reverse(nums,0)
            return
        
        #the first number that is greater than nums at index1
        index2 = n-1
        while index2 >= 0:
            if nums[index2] <= nums[index1]:
                index2 -= 1
            else:
                break
     
        #swap
        nums[index1], nums[index2] = nums[index2], nums[index1]
        reverse(nums, index1+1)
        