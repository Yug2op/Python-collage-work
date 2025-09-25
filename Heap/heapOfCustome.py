import heapq

class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} {self.age}"
    
    def __lt__(self,other):
        return self.age > other.age
        
l = [Customer("aryabhatta",74),Customer("Rmanujan",64),Customer("Homi",84)]
heapq.heapify(l)

while l:
    print(heapq.heappop(l))