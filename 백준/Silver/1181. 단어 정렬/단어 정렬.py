n = int(input())
words = []

for _ in range(n):
    word = input()
    if word not in words:
        words.append(word)

for i in sorted(words, key=lambda x: (len(x), x)):
    print(i)