def replace(s,i,out,result):
    if i == len(s):
        result.append(out)
        return
    if s[i] == '?':
        replace(s,i+1,out+'0',result)
        replace(s,i+1,out+'1',result)
    else:
        replace(s,i+1,out+s[i],result)
        
t = int(input())
for i in range(t):
    result = []
    s = input()
    replace(s,0,"",result)
    for res in result:
        print(result,end=" ")