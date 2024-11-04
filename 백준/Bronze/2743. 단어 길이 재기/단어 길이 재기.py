while True:
    try:
        word = input()
        print(len(word))
    except EOFError:
        break