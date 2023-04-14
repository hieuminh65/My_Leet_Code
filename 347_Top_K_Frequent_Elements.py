class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        setR = {}
        for n in nums:
            setR[n] = setR.get(n, 0) + 1
        result = []
        sorted_dict = sorted(setR.items(), key=lambda x: x[1], reverse=True) 
        for i in range(k):
            result.append(sorted_dict[i][0])

        return result