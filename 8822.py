# I method

def solve():
    n = int(input())
    ans = 1
    for i in range(1, n + 1):
        if i == n and i != 1:
            k = 9
        elif i == n and i == 1:
            k = 8
        elif i == 1:
            k = 8
        else:
            k = 9
        ans *= k
    print(ans)
solve()

# II method

def count(n):
    if n != 1:
        s = 8 * (9 ** (n - 1)) 
        return s
    else:
        return 8

n = int(input())
print(count(n))
