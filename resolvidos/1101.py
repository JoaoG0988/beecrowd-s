
n = 1

while n > 0:
    soma = 0
    m,n = map(int, input().split())
    if m > n and m > 0 and n >0:
        lista = []
        for i in range(n,m+1):
            lista.append(i)
            soma += i
        print(*lista, end=" ")
        print(f'Sum={soma}')

    if m < n and m > 0 and n > 0:
        lista = []
        for j in range(m,n+1):
            lista.append(j)
            soma += j
        print(*lista, end=" ")
        print(f'Sum={soma}')

    if n <= 0 or m <= 0:
        break