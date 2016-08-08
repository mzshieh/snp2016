# Guess a digit

import random

# Pick the answer randomly
ans = random.randint(0,9)

print('I prepared a secret digit (from 0 to 9).')
print('Guess what it is. You have 5 chances.')

for i in range(5): # five chances
    
    print('Round '+str(i+1))

    # Read a digit to x
    x = None
    while True:
        try:
            x = int(input('Guess a digit: '))
        except: # Error handler
            print('Please give me an integer')
            continue
        
        # check if x is a digit
        if x >= 0 and x <= 9:
            break
        print('Please give me a digit')
    
    # Check if the answer is correct. If not, give a hint.
    if x > ans:
        print('The answer is less than '+str(x))
    elif x < ans:
        print('The answer is greater than '+str(x))
    else:
        print('The answer is '+str(x))
        print('Congrats!')
        break

# post game process
if i == 0: # Find the answer immediately
    print('Did you cheat?')
elif x == ans: # Find the answer in multiple rounds
    print('You give the correct answer in '+str(i+1)+' rounds')
else: # reveal the answer
    print('The answer is '+str(ans))