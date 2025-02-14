i = 0

soma = 0

lista = []
while i < 2:
    nota = float(input())
    if nota >=0 and nota <= 10:
        i += 1
        lista.append(nota)
        if len(lista) >= 2:
            media = sum(lista)/len(lista) 
            print(f'media = {media:.2f}')
            break
        
    else:
        print('nota invalida')