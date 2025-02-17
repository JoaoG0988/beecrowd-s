num = int(input())


for i in range(num):
    string = input().split()
    string.sort(key = len, reverse = True)
    
    print(' '.join(string))
        