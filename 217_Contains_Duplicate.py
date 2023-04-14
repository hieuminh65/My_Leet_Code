class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        setn = set(nums)
        if len(setn) == len(nums):
            return False
        else:
            return True