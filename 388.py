def count_changes(n):
  count = 0
  while n != 1:
    if n % 2 == 0:
      n //= 2
    else:
      n += 1
    count += 1
  return count
number = int(input())
result = count_changes(number)
print(result)