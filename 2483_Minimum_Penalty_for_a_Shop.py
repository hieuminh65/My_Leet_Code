class Solution:
    def bestClosingTime(self, customers: str) -> int:

        maxS = 0
        min_hour = -1 
        score = 0
        for i, c in enumerate(customers):
            if c == 'Y':
                score +=1 
            else:
                score -=1 
            if score > maxS:
                maxS = score
                min_hour = i
        return min_hour + 1