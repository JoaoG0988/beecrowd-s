cod,quant = input().split()
cod = int(cod)
quant = int(quant)

if cod == 1:
    valor = 4.00
if cod == 2:
    valor = 4.50
if cod == 3:
    valor = 5.00
if cod == 4:
    valor = 2.00
if cod == 5:
    valor = 1.50

total =  quant * valor

print(f'Total: R$ {total:.2f}')