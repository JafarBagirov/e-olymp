 
n = int(input())
arr = list(map(int, input().split()))
odd_index_elements = [arr[i] for i in range(1, n, 2)]
if odd_index_elements:
    print(len(odd_index_elements))
    print(*odd_index_elements)
else:
    print("NO")