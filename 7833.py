 
n = int(input())
l = list(map(int, input().split()))
average = sum(l) / n
greater_than_avg = [x for x in l if x > average]
count_greater = len(greater_than_avg)
sum_greater = sum(greater_than_avg)
print(sum_greater, count_greater)