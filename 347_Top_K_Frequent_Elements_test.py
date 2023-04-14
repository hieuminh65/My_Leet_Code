def topKFrequent(nums, k):
        
        setR = {}
        for n in nums:
            setR[n] = setR.get(n, 0) + 1
        result = []
        print(setR)
        sorted_dict = sorted(setR.items(), key=lambda x: x[1], reverse=True) 
        print(sorted_dict)
        for i in range(k):
            result.append(sorted_dict[i][0])

        return result

n = topKFrequent([-1,-1], 1)
print(n)
m =topKFrequent([1,1,1,2,2,3,4,4,4,4,4], 2)
print(m)
