n_arr = list(map(str, input().split('-')))

sum = 0

for i in n_arr[0].split('+') :
    sum += int(i)

for i in n_arr[1:] :
    for j in i.split('+') :
        sum -= int(j)

print(sum)