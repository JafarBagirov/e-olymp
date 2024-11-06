s = input()
s = s.lstrip('-').lstrip('+')
length = len(s)
count = 0
for i in range(length):
    if s[i] in ['+', '-', '*']:
        count += 1
print(count)