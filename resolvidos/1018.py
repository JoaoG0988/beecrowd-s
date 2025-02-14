valor = int(input())

notas = [100,50,20,10,5,2,1]

print(valor)

for i in range(len(notas)):
    if valor >= notas[i]:
        print(f'{valor//notas[i]} nota(s) de R$ {notas[i]},00')
        valor = valor%notas[i]

    else:
        print(f'0 nota(s) de R$ {notas[i]},00')