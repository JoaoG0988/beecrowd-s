x = int(input())
i = 1

while x != 0:
    while i < x:
        print(f'{i} ', end = "")
        i += 1
            

    print(f'{i}')
    i = 1
    x = int(input())