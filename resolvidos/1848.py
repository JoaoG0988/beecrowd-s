piscadas = input()

soma = 0
c = 0

continuar = True

while continuar == True:
    if piscadas == "--*":
        soma += 1
    if piscadas == "*--":
        soma += 4
    if piscadas == "-*-":
        soma += 2
    if piscadas == "***":
        soma += 7
    if piscadas == "-**":
        soma += 3
    if piscadas == "**-":
        soma += 6
    if piscadas == "*-*":
        soma += 5

    elif piscadas == "caw caw":
        print(soma)

        soma = 0

        c += 1

    if c == 3:
        break

    piscadas = input()