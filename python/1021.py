n = float(input())

notas = [100,50,20,10,5,2]
moedas = [1.00,0.50,0.25,0.10,0.05,0.01]

print('NOTAS:')
for i in range(len(notas)):
    quant = 0
    while n - notas[i] >= 0:
        quant += 1
        n -= notas[i]
    print(f'{quant} nota(s) de R$ {notas[i]:.2f}')

print('MOEDAS:')

for i in range(len(moedas)):
    quant = 0
    while n - moedas[i] >= 0:
        quant += 1
        n = float(format(round(n - moedas[i],2)))
    print(f'{quant} moeda(s) de R$ {moedas[i]:.2f}')