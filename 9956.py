 
n = int(input())
s = list(map(int, input().split()))
even_numbers = [x for x in s if x % 2 == 0]
if even_numbers:
    print(max(even_numbers))
else:
    print("NO")