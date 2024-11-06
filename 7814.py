 
def solve():
    s = input()
    a = (int(s[0]) * 10) + int(s[1])
    b = (int(s[0]) * 10) + int(s[2])
    c = (int(s[1]) * 10) + int(s[2])
    a = 100 if a < 10 else a
    b = 100 if b < 10 else b
    c = 100 if c < 10 else c
    print(min(a, b, c))
solve()