 
n,m = map(int, input().split())
mini = 10**(n - 1)
maks = 10**n - 1
if m <= mini:
    s = 0
elif m > maks:
    s = maks - mini + 1
else:
    s = m - mini
print(s)