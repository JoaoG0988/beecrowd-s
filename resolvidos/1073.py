n = int(input())

if 5 < n < 2000:
    for numero in range(1,n+1):
        numero = int(numero)
        if numero % 2 == 0:
            valor = numero**2
            print(f'{numero:.0f}^2 = {valor:.0f}')