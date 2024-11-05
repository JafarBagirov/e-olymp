
x,y=map(float, input().split())
s=(x*x+y*y)**0.5/(x-y)**2-(2*x*y)/(x*x+y*y)**0.5
print(s)