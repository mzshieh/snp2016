# Bull and Cow

def valid(number):
    try:
        number = int(str(number))
        d1 = number % 10
        d2 = number // 10 % 10
        d3 = number // 100 % 10
        d4 = number // 1000 % 10
        return d1 != d2 and d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4 and d3 != d4
    except:
        return False
        
def countA(x,y):
    ret = 0
    if x % 10 == y % 10:
        ret = ret + 1
    if x // 10 % 10 == y // 10 % 10:
        ret = ret + 1
    if x // 100 % 10 == y // 100 % 10:
        ret = ret + 1
    if x // 1000 % 10 == y // 1000 % 10:
        ret = ret + 1
    return ret

def checkB(d,y):
    if d == y % 10 or d == y // 10 % 10 or d == y // 100 % 10 or d == y // 1000 % 10:
        return 1
    return 0

def countB(x,y):
    ret = -countA(x,y)
    ret = ret + checkB(x % 10,y)
    ret = ret + checkB(x // 10 % 10, y)
    ret = ret + checkB(x // 100 % 10, y)
    ret = ret + checkB(x // 1000 % 10, y)
    return ret

import random

# Pick the answer randomly
ans = 0
while not valid(ans):
    ans = random.randint(123,9876)


print('I prepared a 4-digit number. Any of its digits does not repeat.')
print('Guess what it is. You have 10 chances.')

for i in range(10):
    
    print('Round '+str(i+1))

    # Read 4-digit number to x
    x = None
    while True:
        try:
            x = int(input('Guess 4 digits: '))
        except: # Error handler
            print('Please give me an integer')
            continue
        
        # check if x is a digit
        if valid(x):
            break
        print('Please give me four digits')
    
    A = countA(ans, x)
    B = countB(ans, x)
    
    # Check if the answer is correct. If not, give a hint.
    if A < 4:
        print('%dA%dB' % (A,B))
    else:
        print('Congrats!')
        break

if i == 0: # Find the answer immediately
    print('Did you cheat?')
elif x == ans: # Find the answer in multiple rounds
    print('You give the correct answer in '+str(i+1)+' rounds')
else: # reveal the answer
    print('The answer is %04d' % ans)