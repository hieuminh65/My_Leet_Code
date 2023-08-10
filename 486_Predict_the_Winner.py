class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        # compare middle and 
        middle = nums[len(nums) // 2]
        player1 = 0
        player2 = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] > nums[right]:
                player1 += nums[left]  
                left +=1
            else:
                player1 += nums[right]  
                right -=1
            if left == right:
                break

            if nums[left] > nums[right]:
                player2 += nums[left]  
                left +=1
            else:
                player2 += nums[right]  
                right -=1
        print(player1, player2)
        return player1 >= player2
        

Solution = Solution()
nums = [2,4,55,6,8]
print(Solution.PredictTheWinner(nums))