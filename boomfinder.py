# import the library
from appJar import gui
import random

x = 10
y = 10
z = 2
size = x*y-1
booms = random.sample(range(0, size), z)
checked = []
def getSurroundBooms(cor):
    if cor not in checked:
        checked.append(cor)
        count = 0
        if cor<=9:
            cor = '0'+str(cor)
        else:
            cor = str(cor)
            
        for boom in booms:
            if(boom<=9):
                boom = '0' + str(boom)
            else:
                boom = str(boom)
            if abs(int(boom[0])-int(cor[0]))<=1 and abs(int(boom[1])-int(cor[1]))<=1:
                count += 1
        if count == 0:
            for i in range(size):
                if(i<=9):
                    i = '0' + str(i)
                else:
                    i = str(i)
                if abs(int(i[0])-int(cor[0]))<=1 and abs(int(i[1])-int(cor[1]))<=1:
                    getSurroundBooms(int(i))
        app.setButton(str(cor),count)
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
        n = getSurroundBooms(int(button))
        #app.setButton(str(button),str(n))
print(booms)
app = gui()
for i in range(y):
        for j in range(x):
            app.addNamedButton("   ",str(i)+str(j), click, i, j)
app.go()
