# Provide a function to compute the offset of certain direction and step size

import math

def offset(direction, step):
    theta = direction * math.acos(-1.0) / 6
    return -step * math.sin(theta), step * math.cos(theta)
    
while True:
    try:
        hour_hand = float(input('Input ihe direction of clock: '))
        print(offset(hour_hand, 100))
    except:
        break
