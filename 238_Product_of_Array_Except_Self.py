class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        if 0 in nums:
            product = 1
            inOf0 = nums.index(0)
            for i in range(len(nums)):
                if i == inOf0:
                    continue
                product *= nums[i]
                nums[i] = 0
            nums[inOf0] = product
            return nums
        product = 1

        for i in range(len(nums)):

            product *= nums[i]

        for i in range(len(nums)):
            nums[i] = product // nums[i]
        return nums



