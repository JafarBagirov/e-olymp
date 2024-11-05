 
n = int(input())
lst = map(int, input().split())
def f(n):
    if n >= 0:
        return n + 2
    return n
res = list(map(f, lst))
for x in res:
    print(x, end=" ")