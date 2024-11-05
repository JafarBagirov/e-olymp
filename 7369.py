 
a, b = map(int, input().split())
first_lucky = a + (3 - a % 7) % 7
if first_lucky > b:
    print(0)
else:
    count = (b - first_lucky) // 7 + 1
print(count)