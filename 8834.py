 
x,y=map(float, input().split())
s=(2*x*y)/(x*x+y*y)**0.5-(x+y-1)**2/(x*y)
print(s)