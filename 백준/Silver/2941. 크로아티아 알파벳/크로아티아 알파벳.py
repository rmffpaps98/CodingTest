w = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c:
    w = w.replace(i, '*')

print(len(w))