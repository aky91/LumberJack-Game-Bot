import numpy as np
from PIL import ImageGrab
import cv2
import keyboard
import time

# game variables
init = False #state of game
sleepTime = 0.15 #wait time before next operation
cycle = 0 #number of iterations
gameDimension = [580, 130, 780,  400] #coordinates of region of interest(ROI)
leftPoint = [247, 42] #position of man's head on left(int ROI)
rightPoint = [247, 163] #position of man's head on right(in ROI)
dirMan = 0 #boolean variable to represent direction 0: left, 1: right

# function ot change direction
def toggleDirection(dirMan):
    if(dirMan == 0): # on left, move to right
        dirMan = 1
        keyboard.press_and_release('right')
    else: # on right, move to left
        dirMan = 0
        keyboard.press_and_release('left')
    return dirMan

#function of cut tree
def cutTree(dirMan):
    if(dirMan == 0): # if on left, press left
        keyboard.press_and_release('left')
    else: # if on right, press right
        keyboard.press_and_release('right')


# function to check if branch is right above the head
def branchAboutToHit(dirMan, leftPoint, rightPoint, screen):
    if(dirMan == 0): # if on left, check pixel value above leftPoint
        return (screen[leftPoint[0] - 10, leftPoint[1]] < 200)
    else: # if on right, check pixel value above rightPoint
        return (screen[rightPoint[0] - 10, rightPoint[1]] < 200)

# main game loop
while(True):

    # fail safe to kill the bot
    if keyboard.is_pressed('down'):
        break

    # run only if up key is pressed
    if keyboard.is_pressed('up'):

        # initialise position with position left
        if init == False:
            print('GAME STARTED')
            keyboard.press_and_release('left')
            time.sleep(sleepTime)
            init = True
            cycle += 1
            continue

        # capture screen and convert into 1D array(gray)
        img = ImageGrab.grab(bbox=gameDimension)
        screen = np.array(img.copy())
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        # change direction or cut tree
        if branchAboutToHit(dirMan, leftPoint, rightPoint, screen):
            toggleDirection(dirMan)
            time.sleep(sleepTime)
        else:
	        cutTree(dirMan)
	        time.sleep(sleepTime)
            
        cycle += 1
        
    # end of if
#end of while
