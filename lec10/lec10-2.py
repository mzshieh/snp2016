# computing the multiplicative inverse of an integer: 5 times

for i in range(5): # let us run this code five times
    try:
        x = 1 / int(input('Please give me an integer: ')) # we ask for an integer

    except ValueError: # invalid  literal for int() with base 10
        print('This is not an integer')
        continue

    except ZeroDivisionError: # input is zero
        print('zero does not have any multiplicative inverse')
        continue
    
    print('The multiplicative inversie is about ' + str(x))