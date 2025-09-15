def permutation(inp,i):

    # base case:
    if i == len(inp):
        print("".join(inp))
        return 

    # recursive case:
    for j in range(i,len(inp)):
        inp[i],inp[j] = inp[j],inp[i]
        permutation(inp,i+1)
        inp[i],inp[j] = inp[j],inp[i]

s = "abc"
inp = list(s)
permutation(inp,0)