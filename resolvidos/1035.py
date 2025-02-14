def validacao(a, b, c, d):
    if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
        return True

a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

teste = validacao(a,b,c,d)

if teste == True:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')