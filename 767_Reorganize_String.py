from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        
        mapS = [(-v, k) for k,v in count.items()]
        heapq.heapify(mapS)
        res = []
        prev_count = 0
        prev_s = ""

        while mapS:
            count, char = heapq.heappop(mapS)

            res.append(char)

            if prev_count < 0:
                heapq.heappush(mapS, (prev_count, prev_s)) 

            prev_count, prev_s = count + 1, char

        return "".join(res) if len(s) == len(res) else ""