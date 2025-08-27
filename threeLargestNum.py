list = [50, 20, 30, 10, 40, 70, 60]
# 1st way
list.sort()
print("Three largest numbers are:", list[-3:])

# 2nd way
fmsf = float('-inf')
smsf = float('-inf')
tmsf = float('-inf')

for ele in list:
    if ele>fmsf:
        tmsf = smsf
        smsf = fmsf
        fmsf = ele
    elif ele>smsf:
        tmsf = smsf
        smsf = ele
    elif ele>tmsf:
        tmsf = ele
largest = [fmsf, smsf, tmsf]
print("Three largest numbers are:", largest)