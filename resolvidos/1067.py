numero = int(input())
if 1 <= numero <= 1000:
    for i in range(numero + 1):
        if i % 2 != 0:
            print(i)