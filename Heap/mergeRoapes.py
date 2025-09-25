import heapq

l = [4,3,2,6]

heapq.heapify(l)

total = 0
while len(l) > 1:
    a = heapq.heappop(l)
    b = heapq.heappop(l)
    total += (a+b)
    heapq.heappush(l,a+b)
print(total)
# time:O(nlogn)
# time:O(n)

