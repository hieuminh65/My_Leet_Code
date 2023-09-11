class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:

        s = set()
        for start, end in nums:
            s |= (set(range(start,end+1)))
        return len(s)
            
        
s = Solution()
# nums = [[3,6],[1,5],[4,7]]
nums = [[1,3],[5,8]]
# nums = [[1,5],[3,6],[4,7]]
print(s.numberOfPoints(nums))