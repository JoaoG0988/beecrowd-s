num  = int(input())
l = []

vetor = map(int,input().split())

for i in range(num):
    for valor in vetor:
        l.append(valor)

l2 = list(sorted(l))

if l2[0] in l:
    pos = l.index(l2[0])
    
print(f'Menor valor: {l2[0]}')
print(f'Posicao: {pos}')