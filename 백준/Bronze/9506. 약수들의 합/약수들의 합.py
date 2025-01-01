while True:
    n = int(input())

    if n == -1:
        break

    arr = [i for i in range(1, n) if n % i == 0]

    if sum(arr) == n:
        print(f"{n} = " + " + ".join(map(str, arr)))
    else:
        print(f"{n} is NOT perfect.")