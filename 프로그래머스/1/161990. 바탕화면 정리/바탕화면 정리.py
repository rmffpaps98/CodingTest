def solution(wallpaper):
    x = []
    y = []
    
    for xi, i in enumerate(wallpaper) :
        for yi, j in enumerate(i) :
            if j == "#" :
                x.append(xi)
                y.append(yi)
                
    return [min(x), min(y), max(x)+1, max(y)+1]