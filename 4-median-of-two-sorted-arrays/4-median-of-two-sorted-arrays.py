class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 == 0:
            middle = len(nums)//2
            print(middle)
            return(nums[middle-1] + nums[middle])/2
        else:
            middle = len(nums)//2
            return nums[middle]
        