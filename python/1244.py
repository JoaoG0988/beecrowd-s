num = int(input())


for i in range(num):
    string = input().split()
    n = len(string)
    for i in range(n):
        for j in range(0,n-i-1):
            if len(string[j]) < len(string[j+1]):
                string[j],string[j+1] = string[j+1],string[j]
        
    print(' '.join(string))
        

     

            
        
        
        
        
        