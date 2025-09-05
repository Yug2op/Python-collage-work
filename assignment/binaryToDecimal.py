binary = int(input())
dec = 0
for i in range(len(str(binary))):
    dec = dec + (binary % 10) * pow(2, i)
    binary = binary // 10
print(dec)