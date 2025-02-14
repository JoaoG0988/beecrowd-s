n = int(input())


for i in range(n):
    numeros = [int(num) for num in input().split(" ")]
    x = min(numeros)
    y = max(numeros)
    soma = 0
    for j in range(x+1,y):
        if j % 2 == 1:
            soma += j
    print(soma)