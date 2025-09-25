import heapq

l = []
heapq.heappush(l,(1,2))
heapq.heappush(l,(2,4))
heapq.heappush(l,(2,3))
heapq.heappush(l,(1,0))
heapq.heappush(l,(4,5))

print(l)

while l:
    print(heapq.heappop(l))