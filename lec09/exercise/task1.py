# read a float
a = input()
a = float(a)

# Idea
# step 1: test if a is negative
# Negative: int(a) >= a
# Positive: int(a) <= a

if (a < 0): # a is negative
    if (a-int(a) == -0.5): # 5 to even
        if (int(a) % 2 == 0):
            print(int(a)) # even is up
        else:
            print(int(a)-1) # even down
    elif (a-int(a) < -0.5): # <5 drop
        print(int(a)-1)
    else: # >5 up
        print(int(a))
elif (a > 0):
    if (a-int(a) == 0.5):
        if (int(a) % 2 == 0):
            print(int(a))
        else:
            print(int(a)+1)
    elif (a-int(a) < 0.5):
        print(int(a))
    else:
        print(int(a)+1)    
else:
    print('0')
    
