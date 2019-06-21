# import the library
from appJar import gui
import random

x = 10
y = 20
z = 10
size = x*y-1
booms = random.sample(range(0, size), z)
left_boundary_checker = [-1,x,-x,x-1,-x-1]
right_boundary_checker = [1,x,-x,x+1,-x+1]
normal_checker = list( dict.fromkeys(left_boundary_checker + right_boundary_checker) )

checked = []
#Check the surrending cells, change the current cell name to the number of booms
#in surrending cells. if cell surrending count is 0, check the surrending cells' booms recursively
#only check a cell once.

def getSurroundings(cor, checker):
    surroundings = []
    count = 0
    for e in checker:
        index = cor-e
        if index>=0 and index <=size:
            surroundings.append(index)
    #print(surroundings)
    for cell in surroundings:
        if checkBoom(cell):
            count += 1
    if count == 0:
        for cell in surroundings:
            getSurroundBooms(cell)
    return count

def getSurroundBooms(cor):
    count = 0
    if cor not in checked:
        checked.append(cor)
        # left most cells
        if cor%x == 0:
            count = getSurroundings(cor, left_boundary_checker)
        # right most cells
        elif cor%x==(x-1):
            count = getSurroundings(cor, right_boundary_checker)
        else:
            count = getSurroundings(cor, normal_checker)
        
        cors = str(cor)
        #print(cors)
        app.setButton(cors,count)
        return count

def checkBoom(cor):
    if cor in booms:
        return True
    return False

def click(button):
    print(button)
    if checkBoom(int(button)):
        print('dead')
    else:
        getSurroundBooms(int(button))
app = gui()
print(booms)
for i in range(y):
        for j in range(x):
            btnname = i*x+j
            app.addNamedButton("   ",str(btnname), click, i, j)

app.go()
