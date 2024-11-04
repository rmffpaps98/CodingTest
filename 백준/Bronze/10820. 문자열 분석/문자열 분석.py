while True:
    try:
        n = input()
        low, up, num, emp = 0, 0, 0, 0
        for i in n:
            if ord(i) >= 65 and ord(i) <= 90:
                up += 1
            elif ord(i) >= 97 and ord(i) <= 122:
                low += 1
            elif i in '1234567890':
                num += 1
            else:
                emp += 1
        print(low, up, num, emp)
    except EOFError:
        break