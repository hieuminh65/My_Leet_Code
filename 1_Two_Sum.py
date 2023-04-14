
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] +nums[j] == target):
                return [i,j]
    return False

print(twoSum([2,3,4,5],7))
# length = 4