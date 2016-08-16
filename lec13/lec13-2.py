import operator, math, pyautogui, time

# some math
PI = math.acos(-1.0)

# some other math
def rotate(pt,theta):
    x, y = pt
    return (math.cos(theta)*x-math.sin(theta)*y,math.sin(theta)*x+math.cos(theta)*y)

# just offset pt by off
def offset(pt,off):
    return (pt[0]+off[0],pt[1]+off[1])

# return the branches if level is not too large
# You should not look into it
def branch_list(level, size):
    if level > 4:
        return branch_list(4,size)
    if level == 0:
        return [(0,0),(0,-size),(0,0)]
    
    branchlet = branch_list(level-1, 0.5*size)
    
    ret = [(0,0)]
    ret += [offset(pt,(0,-0.5*size)) for pt in [rotate(p,PI/4) for p in branchlet]]
    ret += [offset(pt,(0,-1.0*size)) for pt in [rotate(p,PI/8) for p in branchlet]]
    ret += [offset(pt,(0,-0.8*size)) for pt in [rotate(p,-PI/6) for p in branchlet]]
    ret += [offset(pt,(0,-0.6*size)) for pt in [rotate(p,-PI/3) for p in branchlet]]
    ret += [(0,0)]
    return ret

# Draw along the coordinates in the list
def draw_list(the_list):
    for pt in the_list:
        pyautogui.dragTo(pt[0],pt[1])

# The entry point of the program
pyautogui.click() # focus on the canvas of Microsoft Paint
time.sleep(0.5) # Wait

branch = [(0,0),(0,-100),(60,-180),(0,-100),(-60,-180),(0,-100),(0,0)]
# branch = branch_list(3,200)

pos = [offset(pt,pyautogui.position()) for pt in branch]
draw_list(pos)
