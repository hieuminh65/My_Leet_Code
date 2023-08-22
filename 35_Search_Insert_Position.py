class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        print(mid, low, high)
        if nums[mid] < target:
            return mid + 1
        else:
            if mid - 1 < 0:
                return 0
            else:
                return mid - 1
            
s = Solution()

print(s.searchInsert([1,3,5,6], 2))