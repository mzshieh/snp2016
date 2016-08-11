# to help you play 4-digit bull and cow

def num_to_digits(number):
    ret = []
    for i in range(4):
        digit = number % 10
        ret.append(digit)
        number = number // 10
        
    return ret

# return whether number is valid: four digits are different
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

# Read an integer from standard input
def get_int(name):
    while True:
        try:
            return int(input('input an integer ' + name + ': '))
        except:
            # you may also try pass statement here
            # pass
            continue

# maintain a list of candidate
candidate = []
# try all 2-digit numbers: all valid number are candidates
for i in range(10000):
    if valid(i):
        candidate.append(i)

# the helper loop terminates when the answer is revealed.
while len(candidate) > 1:
    # input game information
    x = get_int('x')
    A = get_int('A')
    B = get_int('B')
    
    # the candidates passing this test should be put in new_candidate
    new_candidate = []
    for i in candidate:
        if countA(x,i) == A and countB(x,i) == B:
            new_candidate.append(i)
    candidate = new_candidate
    print(candidate)

if len(candidate) == 1:
    print('the answer is '+str(candidate[0]))
else:
    print('no answer! the program is cheating!')