x,y = input().split()
x = float(x)
y = float(y)

if x > 0 and y < 0:
    print('Q4')
if x < 0 and y > 0:
    print('Q2')
if x < 0 and y < 0:
    print('Q3')
if x > 0 and y > 0:
    print('Q1')

if x == 0 and y == 0:
    print('Origem')

if x != 0 and y == 0:
    print('Eixo X')

if y != 0 and x == 0:
    print('Eixo Y')