
n = int(input())

total = 0
c = 0
r = 0
s = 0


dicio = {}

for i in range(n):
    quant,animal = input().split()
    quant = int(quant)
    total += quant
    dicio[animal] = int(quant)

    if animal == "C":
        c += dicio[animal]
    if animal == "R":
        r += dicio[animal]
    if animal == "S":
        s += dicio[animal]

c1 = (c/total) * 100
r1 = (r/total) * 100
s1 = (s/total) * 100


print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {c1:.2f} %')
print(f'Percentual de ratos: {r1:.2f} %')
print(f'Percentual de sapos: {s1:.2f} %')