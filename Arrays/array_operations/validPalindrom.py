s = "0p"
cap = s.upper()
st = ""
for ch in cap:
    if 65 <= ord(ch) <= 90:
        st = st+ch

i = 0
j = len(st)-1
while i < j:
    if st[i] == st[j]:
        i += 1
        j -= 1
    else:
        print( False  )
print(True)  
