inicial,final = map(int, input().split())

if inicial == final:
    h = 24
elif inicial <= final:
    h = final - inicial
else:
    h = (24-inicial) + final

print(f'O JOGO DUROU {h} HORA(S)')