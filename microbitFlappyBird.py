from microbit import *
from random import *
import music


class Wall:
    column = -1
    hole = -1


birdRow = 2
BIRD_COLUMN = 1
birdCanMove = True
birdBrightness = 9
score = 0
WALL_MOVE_TIMER = 800
WALL_BRIGHTNESS = 3
EMPTY_ROW = "00000"
wallMoveTimer = WALL_MOVE_TIMER
walls = []
wallsUpdated = True
gamePlaying = True


def moveUp():
    global birdRow
    if birdRow > 0:
        birdRow -= 1
    updateDisplay()
    return


def moveDown():
    global birdRow
    if birdRow < 4:
        birdRow += 1
    updateDisplay()
    return


def addAWall():
    global walls
    newWall = Wall()
    newWall.column = 5
    newWall.hole = randint(0, 4)
    walls.append(newWall)
    return


#this function controls the data for positioning the walls but not displaying
def moveWalls():
    global score
    for wall in walls:
        wall.column -= 1
        #when a wall is in the first column, it is time to add a new one
        if(wall.column==BIRD_COLUMN and wall.hole!=birdRow):
            gameOver()
            return
        if(wall.column == 0):
            addAWall()          
            #add a point to the score and play a score sound
            score += 1         
            music.play(music.BA_DING)
        if(wall.column < 0):
            #delete the wall from the list
            del walls[0]
    updateDisplay()
    return


def updateDisplay():
    screenContents = ""
    #move the bird up and down
    for row in range(0, 5):
        nextRow = EMPTY_ROW
       
        for wall in walls:
          wallColumn = wall.column
          hole = wall.hole
          if(row!=hole):
            nextRow = nextRow[:wallColumn]+str(WALL_BRIGHTNESS)+nextRow[wallColumn:]
        if(row != 4):
            nextRow += ":"
        #draw the bird
        if(birdRow == row):            
            nextRow = nextRow[:BIRD_COLUMN]+str(birdBrightness)+nextRow[BIRD_COLUMN+1:]
        #go through and add the walls
        screenContents += nextRow
    display.show(Image(screenContents))
    return


def gameOver():
    global gamePlaying
    gamePlaying = False
    display.show(Image.SKULL)
    sleep(1000)
    display.scroll("Score: "+str(score), delay=100,loop=True)
    return
    
    
#add an initial wall
addAWall();

#Update each frame
while gamePlaying:    
    if button_a.is_pressed() and birdCanMove is True:
        birdCanMove = False
        moveUp()
    elif button_b.is_pressed() and birdCanMove is True:
        birdCanMove = False
        moveDown()
    if not button_a.is_pressed() and not button_b.is_pressed():
        birdCanMove = True
  
    #decrement the wall timer
    wallMoveTimer -= 1
    #check if walls need to be moved
    if(wallMoveTimer==0):
        moveWalls()
        wallMoveTimer = WALL_MOVE_TIMER
