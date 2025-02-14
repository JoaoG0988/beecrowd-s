num = float(input())

if num >= 0:
    
    nc_num = format(num, "+.4E")

    print(nc_num)
    
else:
    nc_num = format(num, "-.4E")
    print(nc_num)
    