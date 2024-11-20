from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        res = 0

        curSum = 0
        curM = defaultdict(int)
        l = 0

        for r, n in enumerate(nums):
            curSum += n
            curM[n] += 1

            # remove the left element
            if r - l + 1 > k:
                curSum -= nums[l]
                curM[nums[l]] -= 1
                if curM[nums[l]] <= 0:
                    del curM[nums[l]]
                l += 1

            if len(curM) == k:
                res = max(res, curSum)

        return res