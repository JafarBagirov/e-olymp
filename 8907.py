 
n = int(input())
k = 1
while k**3 < n:
    k += 1
    largest_cube = (k - 1) ** 3
print(largest_cube)