def s(n):
    count_A = 0
    count_AB = 0
    count_ABA = 0
    
    for char in n:
        if char == 'A':
            count_ABA += count_AB
            count_A += 1
        elif char == 'B':
            count_AB += count_A
    
    return count_ABA

n = input()
print(s(n))
