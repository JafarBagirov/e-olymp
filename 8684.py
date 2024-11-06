def solve():
    numbers = list(map(int, input().split()))
    ans = len(numbers)
    total_sum = sum(numbers)
    print(ans, total_sum)
solve()
