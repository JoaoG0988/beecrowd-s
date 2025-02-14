
x = int(input())
y = int(input())

lista = [x,y]

x = min(lista)
y = max(lista)


for i in range(x+1,y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
