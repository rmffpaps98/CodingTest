num = []

for _ in range(5):
    num.append(int(input()))

print(sum(num)//5)
print(sorted(num)[len(num)//2])