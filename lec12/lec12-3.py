# Bull and Cow: 4-digit version

def num_to_digits(number):
    ret = []
    for i in range(4):
        digit = number % 10
        ret.append(digit)
        number = number // 10
        
    return ret

def valid(number):
    if number < 0 or number > 9999:
        return False
        
    digits = num_to_digits(number)
    for i in range(4):
        for j in range(4):
            if i != j and digits[i] == digits[j]:
                return False

    return True


def countA(x,y):
    ret = 0
    x_digits = num_to_digits(x)
    y_digits = num_to_digits(y)
    
    for i in range(4):
        if x_digits[i] == y_digits[i]:
            ret = ret + 1
    
    return ret

def countB(x,y):
    ret = 0
    x_digits = num_to_digits(x)
    y_digits = num_to_digits(y)
    
    for i in range(4):
        if x_digits[i] != y_digits[i] and x_digits[i] in y_digits:
            ret = ret + 1

    return ret

import random

# Pick the answer randomly
ans = 0
while not valid(ans):
    ans = random.randint(0,9999)

print('I prepared a secret 2-digit numbers.')
print('Its two digits are different')
print('Guess what it is. You have 10 chances.')

for i in range(10):
    
    print('Round '+str(i+1))

    # Read 4 digit to x
    x = None
    while True:
        # read a string to x
        x = input('Guess: ')
        
        # length check
        if len(x) != 4:
            print('Please give me four digits')
            continue
        
        try:
            x = int(x)
        except: # Error handler
            print('Please give me an integer')
            continue
        
        # check if x is valid
        if valid(x):
            break
        print('Please give me four different digits')
    
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
    print('The answer is %02d' % ans)