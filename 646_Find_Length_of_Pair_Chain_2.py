class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [1] * n
        
        for i in range(1, n):

            dp[i] = max(dp[i], max(dp[j] + 1 if pairs[i][0] > pairs[j][1] else 1 for j in range(i)))
            print(dp)
        print(dp)        
        return max(dp)
    
s = Solution()
print(s.findLongestChain([[1,3], [2,3], [4,5]]))