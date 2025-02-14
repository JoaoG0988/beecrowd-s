N = int(input())

for i in range(N):
    contador = 0
    i = input()
    for numero in i:
        if numero == '1':
            contador += 2
        if numero == '2':
            contador += 5
        if numero == '3':
            contador += 5
        if numero == '4':
            contador += 4
        if numero == '5':
            contador += 5
        if numero == '6':
            contador += 6
        if numero == '7':
            contador += 3
        if numero == '8':
            contador += 7
        if numero == '9':
            contador += 6
        if numero == '0':
            contador += 6
    print(f'{contador} leds')