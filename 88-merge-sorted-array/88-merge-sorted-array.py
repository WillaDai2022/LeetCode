class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        end = m + n - 1
        idx1 = m - 1
        idx2 = n - 1
        
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[end] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[end] = nums2[idx2]
                idx2 -= 1
                
            end -= 1
                
        while idx2 >= 0:
            nums1[end] = nums2[idx2]
            idx2 -= 1
            end -= 1