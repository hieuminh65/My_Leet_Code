class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        res = 0
        p = 0

        while p + 1 < len(nums):
            print(nums)
            if nums[p] == nums[p+1]:
                nums.remove(nums[p+1])
            else:
                res +=1
                p+=1
        print(nums)
        return res


s = Solution()

print(s.removeDuplicates([1,1,2]))