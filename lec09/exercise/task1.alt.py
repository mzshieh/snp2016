while True:
    # read a float
    try:
        a = input()
        a = float(a)
    except:
        break 

    if (a-int(a)==0.5 or a-int(a)==-0.5):
        if(int(a)%2 == 0):
            print(int(a))
        else:
            print(int(a+a-int(a)))
    elif (a < 0):
        print(int(a-0.5))
    elif (a > 0):
        print(int(a+0.5))
    else:
        print('0')
