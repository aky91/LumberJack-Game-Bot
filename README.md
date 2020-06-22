# LumberJack-Game-Bot
Bot to play LumberJack

LumberJack is an online game played via telegram bot(for more details see https://telegram.games/telegram-games/lumberjack/)

This bot plays the game by analysing the screenshots.

## Prerequisites

### 1. Finding Coordinates of the Region of Interest 
   * Open the Lumberjack Game and take a screenshot. 
   * Find the Region of Interest and get the coordinates of upper left point and bottom right point.
   * Update the values in the game variable "gameDimension"
   
### 2. Finding Coordinates of Game Character's Head on the left and right side of the tree
   * Using "img.show()" see the image captured and get the coordinates of head position on the left and right side of the tree
   * Update the values in the game variables "leftPoint" and "rightPoint"
   

## Steps to run

1. Run the python script(make sure that all the imported libraries are available)
2. Open the lumberjack game and click play
3. Keep pressing the &uparrow; key to play
4. Press &downarrow; to terminate the bot

## Major Challenge
After cutting the tree, how long should the bot wait

### Approach#1: Static wait time
Experimentally found to be around 0.15 second with a max score of 246
Note: This value may differ based on factors like framerate, CPU load, etc.

### Approach#2: Dynamic wait time
Figuring out the amount of decay is challenging
Difficult to find manually

### Approach#3: Monitor change in height of the lowest branch
  Assumption: when the tree is cut, the height of the lowest branch is reduced
  
  Problem: there is a whole animation of tree height reducing
