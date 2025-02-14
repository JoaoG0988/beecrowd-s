soma = 0
c = 0
continuar = True

while continuar == True:
    nota = float(input())

    if nota >= 0.0 and nota <=10:
        soma += nota
        c += 1

        if c == 2:

            media = (soma/c)

            print(f'media = {media:.2f}')
            c = 0
            soma = 0

            while True:
                print('novo calculo (1-sim 2-nao)')
                resp = int(input())
                if resp == 2:
                    continuar = False
                    break
                elif resp == 1:
                    continuar = True
                    break
    else:
        print('nota invalida')