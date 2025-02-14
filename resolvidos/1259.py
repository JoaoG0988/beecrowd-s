
num = int(input())
lista = []

par = []
impar = []

for i in range(num):
    n = int(input())
    lista.append(n)

for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

par.sort()
impar.sort(reverse = True)
#print(impar)

for char in impar:
    par.append(char)
for j in par:
    print(j)