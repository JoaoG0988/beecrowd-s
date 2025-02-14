x,y,z = [int(x) for x in input().split()]

maior = 0


for i in (x,y,z):
    if i > maior:
        maior = i
print(f'{maior} eh o maior')