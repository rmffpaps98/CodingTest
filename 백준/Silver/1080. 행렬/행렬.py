n, m = map(int, input().split())

mat_A = [list(map(int, list(input()))) for _ in range(n)]
mat_B = [list(map(int, list(input()))) for _ in range(n)]

def flip(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            mat_A[x][y] = 1 - mat_A[x][y]

cnt = 0
if (n < 3 or m < 3) and mat_A != mat_B :
    cnt = -1
else :
    for i in range(n-2) :
        for j in range(m-2) :
            if mat_A[i][j] != mat_B[i][j] :
                cnt += 1
                flip(i, j)
                
if cnt != -1:
    if mat_A != mat_B:
        cnt = -1

print(cnt)