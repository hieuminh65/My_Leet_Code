import math
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        cur, res = -math.inf , 0

        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                res +=1
        



        return res