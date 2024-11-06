 
ch = input()
len_ch = len(ch)
answer = 0
for i in range((len_ch - 1) // 2 + 1):
    if ch[i] == ch[len_ch - i - 1]:
        answer += 1
print(answer)