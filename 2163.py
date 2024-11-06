def solve():
    numbers = list(map(int, input().split()))
    total_sum = sum(numbers)
    if total_sum % 3 == 0:
        print("YES")
    else:
        print("NO")
solve()
