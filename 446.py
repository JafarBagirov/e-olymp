n = int(input())
say = 0

for i in range(1, n + 1):
    if n % i == n // i:
        say += 1

print(say)
