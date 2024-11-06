 
n = input()
a,b = map(int, input().split())
print(n[:a] + n[b+1:])