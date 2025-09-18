class stack:
    def __init__(self):
        self.l = []
    def push(self,val):
        self.l.append(val)
    def pop(self):
        return self.l.pop()
    def top(self):
        return self.l[-1]
    def size(self):
        return len(self.l)
    def empty(self):
        return len(self.l) == 0
    
    
s = stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
    
print(s.size())

s.pop()
print(s.top())
print(s.empty())
print(s.size())