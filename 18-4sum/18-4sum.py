class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        elif n == 4:
            return [nums,] if sum(nums) == target else []

        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if sum(nums[i:i + 4]) > target:
                break
            if nums[i] + sum(nums[-3:]) < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if sum(nums[j:j + 3],nums[i]) > target:
                    break
                if nums[i] + nums[j] + sum(nums[- 2:]) < target:
                    continue
                
                # 双指针模板写法
                left, right = j + 1, n - 1
                while left < right:
                
                    sum_4 = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum_4 == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1


                    elif sum_4 > target:
                        right -= 1

                    else:
                        left += 1
        
        return res

