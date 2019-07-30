# import the library
from appJar import gui
import random

x = 30
y = 30
z = 100
size = x*y-1
booms = random.sample(range(0, size), z)
left_boundary_checker = [-1,x,-x,x-1,-x-1]
right_boundary_checker = [1,x,-x,x+1,-x+1]
normal_checker = list( dict.fromkeys(left_boundary_checker + right_boundary_checker) )

app = gui()
checked = []
#Check the surrending cells, change the current cell name to the number of booms
#in surrending cells. if cell surrending count is 0, check the surrending cells' booms recursively
#only check a cell once.
def reset():
    for i in range(size+1):
        app.setButton(str(i),"   ")
    checked[:] = []
    
    
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
        app.setButton(cors,count)
        app.setButtonState(cors,"disabled")
        app.setButtonRelief(cors,"sunken")
        if count == 1:
            app.setButtonDisabledFg(cors, "purple")
        elif count == 2:
            app.setButtonDisabledFg(cors, "blue")
        elif count == 3:
            app.setButtonDisabledFg(cors, "green")
        elif count == 4:
            app.setButtonDisabledFg(cors, "orange")
        elif count == 5:
            app.setButtonDisabledFg(cors, "red")
        return count

def checkBoom(cor):
    if cor in booms:
        return True
    return False

def click(button):
    if checkBoom(int(button)):
        app.infoBox("DEAD", "A hero just set his foot onto a boom.", parent=None)
        #app.stop()
    else:
        getSurroundBooms(int(button))
    if len(checked)==size+1-z:
        app.infoBox("Winner!","Winner Winner, Chiken Dinner!", parent=None)
        

    
for i in range(y):
        for j in range(x):
            btnname = str(i*x+j)
            app.addNamedButton("",btnname, click, i, j)
            app.setButtonWidth(btnname, 2)
            #app.setButtonHeight(btnname, 2)

app.go()
