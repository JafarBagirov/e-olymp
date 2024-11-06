n = int(input())
total_sum = 0
number = 1

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            total_sum += number
        number += 1 
print(total_sum)