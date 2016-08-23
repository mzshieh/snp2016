# Bull and Cow: 2-digit version

def valid(number):
    if number < 0 or number > 99:
        return False
    try:
        d1 = number % 10
        d2 = number // 10
        return d1 != d2
    except:
        return False
        
def countA(x,y):
    ret = 0
    if x % 10 == y % 10:
        ret = ret + 1
    if x // 10 == y // 10:
        ret = ret + 1
    return ret

def countB(x,y):
    ret = 0
    if x % 10 == y // 10:
        ret = ret + 1
    if x // 10 == y % 10:
        ret = ret + 1
    return ret

import random

# Pick the answer randomly
ans = 0
while not valid(ans):
    ans = random.randint(1,98)

print('I prepared a secret 2-digit numbers.')
print('Its two digits are different')
print('Guess what it is. You have 10 chances.')

for i in range(10):
    
    print('Round '+str(i+1))

    # Read a digit to x
    x = None
    while True:
        try:
            x = input('Guess: ')
            if len(x) != 2:
                print('Please give me two digits')
            x = int(x)
        except: # Error handler
            print('Please give me an integer')
            continue
        
        # check if x is a digit
        if valid(x):
            break
        print('Please give me different digits')
    
    A = countA(ans, x)
    B = countB(ans, x)
    
    # Check if the answer is correct. If not, give a hint.
    if A < 2:
        print('%dA%dB' % (A,B))
    else:
        print('Congrats!')
        break

if i == 0: # Find the answer immediately
    print('Did you cheat?')
elif x == ans: # Find the answer in multiple rounds
    print('You give the correct answer in '+str(i+1)+' rounds')
else: # reveal the answer
    print('The answer is %02d' % ans)