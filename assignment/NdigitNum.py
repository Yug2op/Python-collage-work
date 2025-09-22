def num(out,n,last=""):
    # base Case
    if len(out) == n:
        print("".join(out))
        return
    # recursive case
    out.append('a')
    num(out,n,last="a")
    out.pop()
    if last != 'b':
        out.append('b')
        num(out,n,last="b")
        out.pop()
    
    
    


t = int(input())

for _ in range(t):
    n = int(input())
    out = []
    num(out,n)