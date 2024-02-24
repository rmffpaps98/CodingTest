def solution(polynomial):
    answer = ''
    x = 0
    n = 0
    for i in polynomial.split() :
        if "x" in i :
            if i.replace('x', '') :
                x += int(i.replace('x', ''))
            else : x += 1
        elif i.isdigit() : n += int(i)
    
    if x == 0 : return str(n)
    elif  x == 1 : return f"x + {n}" if n != 0 else "x"
    else : return f"{x}x + {n}" if n != 0 else f"{x}x"