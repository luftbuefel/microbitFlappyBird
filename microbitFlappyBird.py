from microbit import *

birdRow = 2
birdColumn = 1
birdCanMove = True

EMPTY_ROW = "00000"

def moveUp():
    global birdRow
    if birdRow<0:
        birdRow-=1
    return

def moveDown():
    global birdRow
    if birdRow<4:
        birdRow+=1
    return

def updateDisplay():
    newDisplay = ""
    nextRow=""
    for row in range(0,4):
        nextRow += EMPTY_ROW
        if(birdRow==row):
            nextRow = EMPTY_ROW[:birdColumn]+"9"+EMPTY_ROW[birdColumn:]
        newDisplay+=nextRow
        if(row != 4):
            nextRow+=":"
    display.show(Image(newDisplay))
    return


while True:
    if button_a.is_pressed():
        moveUp()
    if button_b.is_pressed():
        moveDown()
    #check if the buttons have been upressed
    #if button_a.is_pressed()
    updateDisplay()


