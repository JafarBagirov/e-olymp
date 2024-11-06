def sumNum(s):
    res = sum(int(ch) for ch in s if ch.isdigit())
    return res

def lastNum(s):
    for ch in reversed(s):
        if ch.isdigit():
            return int(ch)
    return 0

def solve():
    s = input().strip()
    last = lastNum(s)
    sum_digits = sumNum(s)

    print("Yes" if sum_digits % 3 == 0 else "No")
    print("Yes" if (sum_digits % 3 == 0) and (last % 2 == 0) else "No")
    print("Yes" if sum_digits % 9 == 0 else "No")


solve()
