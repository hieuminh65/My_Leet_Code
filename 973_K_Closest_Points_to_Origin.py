import heapq
points = [[1,3],[-2,2],[3,6]]

heap = []
for i in range(0, len(points)):
    sumT = points[i][0]**2 + points[i][1]**2
    heap.append([sumT, i])
heapq.heapify(heap)
print(heap)
res = []
k = 1
for _ in range(k):
    e = heapq.heappop(heap)
    res.append(e)
print([points[n] for n in res[1]])
