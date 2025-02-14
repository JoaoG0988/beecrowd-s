n = int(input())

for i in range(n):
    lista = input()
    aberto = 0
    dima = 0
    for j in range(len(lista)):
        if lista[j] == '<':
            aberto += 1
        if lista[j] == '>' and aberto > 0:
            dima += 1
            aberto -= 1

     
    print(dima)