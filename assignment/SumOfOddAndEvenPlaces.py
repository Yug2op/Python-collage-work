num = int(input())

sum_odd = 0
sum_even = 0

digits = [int(d) for d in str(num)]
digits.reverse()
for i in range(len(digits)):
    if (i + 1) % 2 == 0:
        sum_even += digits[i]
    else:
        sum_odd += digits[i]    
print(sum_odd)
print(sum_even)