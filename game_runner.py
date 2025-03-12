# /////////// INSTRUCTIONS /////////////////
# 👾 Let's make the dinosaur game!
# 
# 1️⃣ Run the file & install
#    - in the Terminal run the command: pip3 install pgzero
#    - play the game
#
# 2️⃣ Add in your own charachter & background sprite!
# 
# 3️⃣ Add these features in the game
#     - draw the score on the screen
#     - increase the score each second 
#     - random size obstacles 
# 
# 4️⃣ extension feature ideas
#     - gems : user can collect gems for jump boost and extra coins
#     - obstacles: spawn at random distances
#     - restart: click R to restart the game 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# import required libraries
import pgzrun
from helpers import *
from random import randint

# SETUP SCREEN
WIDTH = 600
HEIGHT = 300
FLOOR_HEIGHT = 260

# SETUP BACKGROUND
background = Actor('background.jpg')

# SETUP PLAYER
player = Actor('alien.png', anchor=('center', 'bottom'))
player.scale = 1         # scales the sprite image
player.x = 30            # sets the X position
player.y = FLOOR_HEIGHT      # sets the Y position
player.speed = 0
player.jump_height = 15
player.gravity = 1

# SETUP OBSTACLE
OBSTARCLE_FILE = "cactus.png"
obstacle_list = []
total_spawn_interval = 100
current_spawn_interval = 0

# SETUP GAME SETTINGS
game_running = True
score = 0

def draw():

  # if the game is running, draw the game
    if game_running == True:

        background.draw()

        player.draw()

        for obstacle in obstacle_list:
          obstacle.draw()

    # else, the game is not running, draw 'Game Over' 
    else:
        screen.draw.filled_rect(Rect((0, 0), (WIDTH, HEIGHT)), (0, 0, 0))
        screen.draw.text(f"Game Over", centerx=WIDTH/2, centery=HEIGHT/2, fontsize= 50)


def key_presses():
    global game_running

    # if the player is on the floor, they can jump
    if player.y == FLOOR_HEIGHT and keyboard[keys.SPACE]:
        player.speed -= player.jump_height

    elif keyboard[keys.ESCAPE]:
        game_running = False


def move_player():
    # move the player
    player.speed += player.gravity
    player.y += player.speed

    # prevent the player from falling below the floor
    if player.y >= FLOOR_HEIGHT:
        player.y = FLOOR_HEIGHT
        player.speed = 0

def obstacle_spawn():
    global current_spawn_interval

    current_spawn_interval += 1

    # if the total spawn interval time has passed, create new obstacle
    if current_spawn_interval > total_spawn_interval:
        # creates a new obstacle
        obstacle = Actor(OBSTARCLE_FILE, anchor=('center', 'bottom'))
        obstacle.scale = 1
        obstacle.x = WIDTH
        obstacle.y = FLOOR_HEIGHT
        obstacle_list.append(obstacle)
        current_spawn_interval = 0

def obstacle_movement():
    # move each obstacle to the left
    for obstacle in obstacle_list:
        obstacle.x -= 10

        # if the obstacle is off the screen, remove it
        if obstacle.x < 0:
            obstacle_list.remove(obstacle)

    ### if player hits a obstacle, end the game
    if player.collidelist(obstacle_list) != -1:
        game_running = True 

def update():
    global game_running

    if game_running == True:
        key_presses()
        move_player()
        obstacle_spawn()
        obstacle_movement()

pgzrun.go()
