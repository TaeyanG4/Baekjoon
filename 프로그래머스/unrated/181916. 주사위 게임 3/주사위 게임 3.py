def solution(a, b, c, d):
    l = len(set([a,b,c,d]))
    if l == 1:
        return a * 1111
    elif l == 2:
        if a==b==c:
            return (10*a+d) ** 2
        elif b==c==d:
            return (10*b+a) ** 2
        elif c==d==a:
            return (10*c+b) ** 2
        elif d==a==b:
            return (10*d+c) ** 2
        else:
            temp = list(set([a,b,c,d]))
            return (temp[0]+temp[1]) * abs(temp[0]-temp[1])
    elif l == 3:
        if a==b:
            return c*d
        elif b==c:
            return d*a
        elif c==d:
            return a*b
        elif d==a:
            return b*c
        elif a==c: 
            return b*d
        elif b==d: 
            return a*c
    else:
        return min(a,b,c,d)
        
    return answer