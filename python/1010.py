p1 = input().split()
p2 = input().split()

p1[1] = int(p1[1])
p1[2] = float(p1[2])
p2[1] = int(p2[1])
p2[2] = float(p2[2])

valor = (p1[1] * p1[2]) + (p2[1] * p2[2])

print(f'VALOR A PAGAR: R$ {valor:.2f}')