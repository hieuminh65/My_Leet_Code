class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n)
        dp[n-1], dp[n-2] = 0, cost[-2]
        print(dp)
        for i in range(n-3, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        print(dp)
        return min(dp[0], dp[1])


s = Solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))