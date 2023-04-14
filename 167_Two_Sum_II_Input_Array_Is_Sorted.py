class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum1 = numbers[l] + numbers[r]
            if sum1 < target:
                l+=1
            elif sum1 > target:
                r-=1
            else:
                break



        return [l +1,r+1]