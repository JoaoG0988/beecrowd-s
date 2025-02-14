
ano = 365

mes = 30

idade = int(input())

idadeano = int(idade/ano)

resto = idade % ano

idademeses = int(resto / mes)

resto2 = int(resto % mes)


print(f'{idadeano} ano(s)')
print(f'{idademeses} mes(es)')
print(f'{resto2} dia(s)')