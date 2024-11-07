def solve():
    n = int(input())
    sum_first = 0 
    sum_second = 0 

    for i in range(n):
        row = list(map(int, input().split()))
        sum_first += row[i]
        sum_second += row[n - i - 1] 

    print(sum_first, sum_second)  

solve()
