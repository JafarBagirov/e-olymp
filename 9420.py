
n, m = map(int, input().split())
maxmax = m - (n - 1)
minmax = (m + n - 1) // n
maxmin = m  // n
print(maxmax, minmax, maxmin)