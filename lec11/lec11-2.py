# Bull and Cow: 2-digit version

# Verify if the number has two different digits
def valid(number):
    # implement the function
    return False
        
# Count how many corresponding digits are the same
def countA(x,y):
    ret = 0
    # implement the function
    return ret

# Count how many digits are common
def countB(x,y):
    ret = 0
    # implement the function
    return ret

import random

# Pick the answer randomly
ans = 0
# implement how to pick a valid answer

print('I prepared a secret 2-digit numbers.')
print('Its two digits are different')
print('Guess what it is. You have 10 chances.')

for i in range(10):
    
    print('Round '+str(i+1))

    # Read a digit to x
    x = None
    # implement: input processing
    
    A = countA(ans, x)
    B = countB(ans, x)
    
    # Check if the input is correct. If not, give a hint.
    if A < 2:
        print('%dA%dB' % (A,B))
    # If the input is correct, then end the game
    # implement: end the game


# reveal the answer if the player cannot solve the puzzle
print('The answer is %02d' % ans)