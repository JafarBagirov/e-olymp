def solve():
    e,f,c  = map(int, input().split())
    
    say = 0
    e = e + f 
    
    while c <= e:
        n = e // c 
        e = n + e % c 
        say = say + n
    
    print(say)

solve()
