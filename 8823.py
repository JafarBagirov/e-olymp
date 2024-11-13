def count_seven(n):
    k = 9 * (10 ** (n - 1))
    s = 8 * (9 ** (n - 1))
    say = k - s
    return say

n = int(input())
print(count_seven(n))
