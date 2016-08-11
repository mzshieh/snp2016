# to help you play 2-digit bull and cow

# return if number is valid: two digits are different
def valid(number):
    if number < 0 or number > 99:
        return False
    return number % 11 != 0

# calculate A
def countA(x,y):
    ret = 0
    if x % 10 == y % 10:
        ret = ret + 1
    if x // 10 == y // 10:
        ret = ret + 1
    return ret

# calculate B
def countB(x,y):
    ret = 0
    if x % 10 == y // 10:
        ret = ret + 1
    if x // 10 == y % 10:
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
for i in range(100):
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