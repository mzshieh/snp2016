for i in range(2,10):
    out = ''
    for j in range(2,6):
        out = out + ' ' +str(j) + 'x' +str(i) +'='+str(i*j)
        if i * j < 10:
            out = out + ' '
        # or you can replace line 4~6 as following
        # out = out + " %dx%d=%2d"%(i, j, i*j)
    print(out)

print()

for i in range(2,10):
    out = ''
    for j in range(6,10):
        out = out + ' ' +str(j) + 'x' +str(i) +'='+str(i*j)
    print(out)

