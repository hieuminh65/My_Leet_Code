class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        network = {}
        for i in range(n):
            network[i] = []
        for road in roads:
            a, b = road
            network[a].append(b)
            network[b].append(a)

        max_rank = 0
        for i in range(n-1):

            for j in range(i+1, n):
                rank = len(network[i]) + len(network[j])
                if i in network[j]:
                    rank -=1
                max_rank = max(rank, max_rank)

        return max_rank