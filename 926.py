 
a,b,c,d,f = map(float, input().split())
s1 = ( a + b + f ) / 2
s2 = (c + d + f) / 2
s_1 = (s1*(s1-a)*(s1-b)*(s1-f))**0.5
s_2 = (s2*(s2-c)*(s2-d)*(s2-f))**0.5
S = s_1+s_2
print(round(S, 4))