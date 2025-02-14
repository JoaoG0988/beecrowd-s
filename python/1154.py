
n = 1

soma = 0
i = 0

while n > 0:
    idades = float(input())
    soma += idades
    i += 1
    if idades < 0:
        soma -= idades
        i -= 1
        break

media = (soma/i)

print(f'{media:.2f}')