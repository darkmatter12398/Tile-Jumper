# Description
Tile-jumper is a 2D platformer that has a series of 5 levels. In each level, you have to go through obstacles and enemeies to eventually reach the flag. Once you reach the 5th levels, you've finished the game

# How to use
1. Install [python](https://www.python.org/)
2. Go to command prompt, and type in the following line to install pygame into your computer:
```bash
pip install pygame
```
3. Run the file "tile_jumper.py"

# Functionality
## Main menu
The main menu consists of 2 buttons: play, and exit. Pressing play will allow you to play the game, and pressing exit will allow you to exit to your desktop.
![image](https://user-images.githubusercontent.com/77501024/211980205-5f832ca3-d06a-46d4-b667-0f1a9d2b8e5a.png)

## Movement
Once the user hits play, an entity will drop down from the sky. This will be the player that the user can control. Use "A" to go left, and "D" to go right. Press spacebar to jump.

![image](https://user-images.githubusercontent.com/77501024/211980746-1958af02-46b7-492a-b2f1-5621b5c28cb5.png)

## GUI
The amount of lives the player has is displayed in the top left corner, and the level the user is in is displayed in the top right corner.
![image](https://user-images.githubusercontent.com/77501024/211981152-0a74c9b0-8788-498d-b525-459ab14d59fa.png)

The screen will also show a game over screen, or a "You win!" screen depending on if the player lost all their lives, or completed level 5.

## Obstacles
The player has 2 main obstacles to go through: traps, and enemies. Enemies are moving around, and if the player makes contact with them, they will lose a life. This also goes for traps, but they are stationary.



![image](https://user-images.githubusercontent.com/77501024/211981382-1416d779-a1ae-41f0-9971-2beebb427432.png)
![image](https://user-images.githubusercontent.com/77501024/211981436-dbdde775-e086-4ab1-84c2-5257fa21f595.png)

If the player falls off a cliff, then they also lose a life.
![image](https://user-images.githubusercontent.com/77501024/211981538-8b9199c5-ff11-47ec-8482-b3ea9625072e.png)

# Level design
Each level has some sort of theme to it, judging by the background picture and the texture of the blocks. They also get progressively harder, but because of the difficulty, the player gains back all their lives after each level is completed

