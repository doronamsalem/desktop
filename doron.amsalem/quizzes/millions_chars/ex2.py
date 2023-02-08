def counte_1_bits(n):
    cnt = 0
    while(n):
        n = n & (n - 1)
        cnt+= 1
    return cnt

print(counte_1_bits(9))
print(counte_1_bits(950))


