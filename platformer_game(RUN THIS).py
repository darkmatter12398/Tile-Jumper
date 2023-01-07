# import necesssary classes and libraries
from player_class import *
from pygame import mixer
import sys

# initialize pygame and screen
pygame.init()
SCREEN_X = 800
SCREEN_Y = 600
USER_SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Tile Jumper")

clock = pygame.time.Clock()

# string files/constants
PLAYER_IDLE_SPRITE = "player_idle.png"
PLAYER_LEFT_SPRITE = "player_left.png"
PLAYER_RIGHT_SPRITE = "player_right.png"
ENEMY_SPRITE = "enemy.png"
GRASS_SPRITE = "grass_tile.png"
PLAY_BUTTON_SPRITE = "play.png"
OPTIONS_BUTTON_SPRITE = "options.png"
QUIT_BUTTON_SPRITE = "quit.jpeg"
SKY_SPRITE = "sky.png"
SPIKE_SPRITE = "spike.png"
GAME_OVER_TEXT_SPRITE = "game_over_text.png"
FLAG_SPRITE = "flag.png"
CITY_SPRITE = "city.png"
PLANK_SPRITE = "plank.png"
HEART_3 = "heart_3.png"
HEART_2 = "heart_2.png"
HEART_1 = "heart_1.png"
RED_SKY_SPRITE = "red_sky.png"
TITLE_SPRITE = "title.png"
PRESS_E_TEXT_SPRITE = "press_e_text.png"
YOU_WIN_TEXT_SPRITE = "you_win_text.png"
SPACE_SPRITE = "space.png"
LEVEL_1_TEXT_SPRITE = "level_1_text.png"
LEVEL_2_TEXT_SPRITE = "level_2_text.png"
LEVEL_3_TEXT_SPRITE = "level_3_text.png"
LEVEL_4_TEXT_SPRITE = "level_4_text.png"
LEVEL_5_TEXT_SPRITE = "level_5_text.png"

# player
player = Player(30, 0, PLAYER_IDLE_SPRITE, USER_SCREEN) # param: (x, y, string file, screen, scale_value)

# buttons
play_button = Button(400, 200, PLAY_BUTTON_SPRITE, USER_SCREEN) # param: (x, y, string file, screen, scale_value)
play_button_clicked = Button(400, 200, PLAY_BUTTON_SPRITE, USER_SCREEN, 2)
quit_button = Button(400, 300, QUIT_BUTTON_SPRITE, USER_SCREEN)
quit_button_clicked = Button(400, 300, QUIT_BUTTON_SPRITE, USER_SCREEN, 2)

# text
game_over_text = Button(400, 300, GAME_OVER_TEXT_SPRITE, USER_SCREEN) # param: (x, y, string file, screen, scale_value)
title_text = Button(400, 80, TITLE_SPRITE, USER_SCREEN, 2)
press_e_text = Button(400, 150, PRESS_E_TEXT_SPRITE, USER_SCREEN, 2)
you_win_text = Button(400, 300, YOU_WIN_TEXT_SPRITE, USER_SCREEN)
level_1_text = Button(670, 30, LEVEL_1_TEXT_SPRITE, USER_SCREEN)
level_2_text = Button(670, 30, LEVEL_2_TEXT_SPRITE, USER_SCREEN)
level_3_text = Button(670, 30, LEVEL_3_TEXT_SPRITE, USER_SCREEN)
level_4_text = Button(670, 30, LEVEL_4_TEXT_SPRITE, USER_SCREEN)
level_5_text = Button(670, 30, LEVEL_5_TEXT_SPRITE, USER_SCREEN)

# background
background_1 = Background(400, 300, SKY_SPRITE, USER_SCREEN) # param: (x, y, string file, screen)
background_2 = Background(1200, 300, SKY_SPRITE, USER_SCREEN)

# class to build levels
builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE, [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12],
                                                                                [11, 12], [12, 12], [13, 12], [14, 12], [15, 12], [16, 12], [7, 11], [7, 10], [8, 10], [8, 11],
                                                                                [9, 11], [9, 10], [9, 9], [10, 11], [10, 10], [10, 9], [11, 11], [11, 10], [11, 9], [11, 8],
                                                                                [12, 11], [12, 10], [12, 9], [12, 8]], [[1, 12]], [[1, 12]], [], USER_SCREEN)

# class to manage physics (e.g. gravity and collision)
physics = Physics(0.75, 20, builder, player)

# scene management (stored as booleans)
menu = True
game = False
game_over = False
you_win = False

# tile velocity for moving tile
tile_x_vel = 0

level_scene = -1 # each level has a scene
max_level_scene = [5, 5, 5, 5, 4] # max level scenes for each level
level = 1 # level int
player_health = 3 # player health int

# music
game_over_music = mixer.Sound("game_over_music.wav")
health_loss_sound = mixer.Sound("health_loss.mp3")
jump_sound = mixer.Sound("jump.wav")
win_sound = mixer.Sound("win.wav")
next_level = mixer.Sound("next_level.mp3")

# main game loop
while True:
        pygame.event.get()
        clock.tick(60)

        # if game is in menu
        if menu == True:
                physics.background_moving(background_1, background_2) # moving background
                builder.draw_tiles() # draws all tiles
                title_text.draw() # draws text

                # if play button is hovered over
                if play_button.button_collision() == True:
                        play_button_clicked.draw()
                        quit_button.draw()

                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN: # if clicked, go to game
                                        menu = False
                                        game = True

                # if quit button is hovered over
                elif quit_button.button_collision() == True:
                        play_button.draw()
                        quit_button_clicked.draw()

                        for event in pygame.event.get(): # if pressed, exit out of pygame
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        sys.exit()

                else:
                        play_button.draw()
                        quit_button.draw()

        # if game over, or player won
        elif game_over == True or you_win == True:

            # draw necessary drawings
            if game_over == True:
                game_over_text.draw()

            if you_win == True:
                you_win_text.draw()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: # if spacebar pressed, go to menu and initalize all necessary variables
                        game_over = False
                        you_win = False
                        menu = True

                        level = 1
                        level_scene = -1
                        player_health = 3

                        background_1 = Background(400, 300, SKY_SPRITE, USER_SCREEN)
                        background_2 = Background(1200, 300, SKY_SPRITE, USER_SCREEN)

                        builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12],
                                                 [7, 12], [8, 12], [9, 12], [10, 12],
                                                 [11, 12], [12, 12], [13, 12], [14, 12], [15, 12],
                                                 [16, 12], [7, 11], [7, 10], [8, 10], [8, 11],
                                                 [9, 11], [9, 10], [9, 9], [10, 11], [10, 10], [10, 9],
                                                 [11, 11], [11, 10], [11, 9], [11, 8],
                                                 [12, 11], [12, 10], [12, 9], [12, 8]], [[1, 12]],
                                                [[1, 12]], [], USER_SCREEN)

                        builder.get_tiles()

        # if game playing
        elif game == True:

                # if certain level
                if level == 1:
                    physics.background_moving(background_1, background_2) # for moving background

                    # if its a certain level scene in a level
                    if level_scene == -1:
                        level_scene = 1

                        # load level tiles
                        builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12],
                                                 [8, 12], [9, 12], [10, 12], [11, 12], [12, 12], [13, 12],
                                                 [14, 12], [15, 12], [16, 12], [7, 11], [7, 10], [8, 10], [8, 11],
                                                 [9, 11], [9, 10], [9, 9], [10, 11], [10, 10], [10, 9], [11, 11],
                                                 [11, 10], [11, 9], [11, 8], [12, 11], [12, 10], [12, 9], [12, 8], [17, 12], [5, 12]],
                                                [], [], [], USER_SCREEN)

                        # update physics object with new tiles
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    elif level_scene == -2:
                            level_scene = 2
                            builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                    [[0, 12], [1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [6, 11], [6, 10],
                                                     [6, 9], [7, 12], [7, 11], [7, 10],
                                                     [7, 9], [8, 12], [8, 11], [8, 10], [8, 9],
                                                     [9, 12], [9, 11], [9, 10],
                                                     [9, 9], [10, 12], [10, 11],
                                                     [10, 10], [10, 9], [11, 12], [12, 12], [13, 12],
                                                     [14, 12], [15, 12], [16, 12], [17, 12]],
                                                    [[8, 9]], [], [], USER_SCREEN)
                            physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    elif level_scene == -3:
                            level_scene = 3
                            builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                    [[0, 12], [1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12],
                                                     [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [14, 12], [15, 12],
                                                     [16, 12], [17, 12]], [[8, 12], [9, 12]], [], [], USER_SCREEN)
                            physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    elif level_scene == -4:
                            level_scene = 4
                            builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                    [[0, 12], [1, 12], [2, 12], [3, 12], [6, 12], [7, 12], [8, 12],
                                                     [9, 12], [10, 12], [11, 12], [12, 12], [12, 11], [12, 10], [13, 12],
                                                     [13, 11], [13, 10], [14, 12], [14, 11], [14, 10], [15, 12], [15, 11],
                                                     [15, 10], [16, 12], [17, 12]], [[14, 10]], [], [], USER_SCREEN)
                            physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    elif level_scene == -5:
                            level_scene = 5
                            builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                    [[0, 12], [1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12],
                                                     [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [14, 12], [15, 12],
                                                     [16, 12], [17, 12]], [], [[10, 12]], [15, 12], USER_SCREEN)
                            physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    if level_scene == 5: # for specific enemy's
                        builder.enemy_list[0].move(5, 500, 150) # specifies where they move and max x value/min x value

                if level == 2:
                    physics.background_moving(background_1, background_2)

                    if level_scene == -1:
                        level_scene = 1
                        builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 12], [2, 12], [3, 12], [4, 12], [4, 11], [4, 10], [4, 9],
                                                 [5, 12], [5, 11], [5, 10], [5, 9], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12],
                                                 [11, 12], [12, 12], [13, 12], [13, 11], [13, 10], [13, 9], [14, 12],
                                                 [14, 11], [14, 10], [14, 9], [15, 12],[16, 12], [17, 12]], [[12, 12]],
                                                [], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    elif level_scene == -2:
                            physics.background_moving(background_1, background_2)

                            level_scene = 2
                            builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                    [[0, 12], [1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12],
                                                     [9, 12], [10, 12], [11, 12], [11, 11], [11, 10], [12, 12], [12, 11], [12, 10] ,
                                                     [13, 12], [13, 11], [13, 10], [14, 12], [14, 11], [14, 10],
                                                     [15, 12], [16, 12], [17, 12]], [[12, 10], [13, 10]], [[8, 12]], [], USER_SCREEN)
                            physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    elif level_scene == -3:
                            level_scene = 3
                            builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                    [[0, 12], [1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12],
                                                     [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [13, 10], [14, 12], [15, 12],
                                                     [16, 12], [17, 12]], [[14, 12], [13, 12], [12, 12]], [[5, 12]], [], USER_SCREEN)
                            physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    elif level_scene == -4:
                            level_scene = 4
                            builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                    [[0, 12], [1, 12], [2, 12], [3, 12], [4, 12], [4, 11], [4, 10], [4, 9],
                                                     [5, 12], [5, 11], [5, 10], [5, 9], [6, 12], [6, 11], [6, 10], [6, 9],
                                                     [7, 12], [8, 12],[9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [14, 12],
                                                     [15, 12],[16, 12], [17, 12]], [[14, 12], [13, 12]], [], [], USER_SCREEN)
                            physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    elif level_scene == -5:
                            level_scene = 5
                            builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                    [[0, 12], [1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12],
                                                     [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [14, 12],
                                                     [14, 11], [15, 12], [16, 12],
                                                     [17, 12]], [], [[14, 11]], [15, 12], USER_SCREEN)
                            physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(), builder.get_flag())

                    if level_scene == 2:
                        builder.enemy_list[0].move(5, 450, 100)

                    elif level_scene == 3:
                        builder.enemy_list[0].move(5, 450, 100)

                if level == 3:
                    background_1 = Background(400, 300, CITY_SPRITE, USER_SCREEN)
                    background_2 = Background(1200, 300, CITY_SPRITE, USER_SCREEN)

                    if level_scene == -1:
                        level_scene = 1
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 8], [1, 12], [1, 11], [1, 10], [1, 9], [2, 12], [2, 11],
                                                 [2, 10], [2, 9], [2, 8], [3, 12], [3, 11], [3, 10], [3, 9], [3, 8],
                                                 [4, 12], [4, 11], [4, 10], [4, 9], [4, 8], [9, 12], [9, 11], [9, 10],
                                                 [9, 9], [9, 8], [10, 12], [10, 11], [10, 10], [10, 9], [10, 8],
                                                 [11, 12], [11, 11], [11, 10], [11, 9], [11, 8], [12, 12], [12, 11], [12, 10], [12, 9], [12, 8],
                                                 [13, 12], [13, 11], [13, 10], [13, 9], [13, 8], [14, 12], [14, 11],
                                                 [14, 10], [14, 9], [14, 8], [15, 12], [15, 11], [15, 10], [15, 9], [15, 8],
                                                 [16, 12], [16, 11], [16, 10], [16, 9], [16, 8], [17, 8]], [], [[11, 8]], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -2:
                        level_scene = 2
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 8], [1, 12], [1, 11], [1, 10], [1, 9], [2, 12], [2, 11], [2, 10], [2, 9],
                                                 [2, 8], [3, 12], [3, 11], [3, 10], [3, 9], [3, 8], [4, 12], [4, 11], [4, 10], [4, 9], [4, 8],
                                                 [9, 12], [9, 11], [9, 10], [9, 9], [9, 8], [10, 12], [10, 11], [10, 10],
                                                 [10, 9], [10, 8], [11, 12], [11, 11], [11, 10], [11, 9], [11, 8], [12, 12],
                                                 [12, 11], [12, 10], [12, 9], [12, 8], [13, 12], [13, 11], [13, 10],
                                                 [13, 9], [13, 8], [14, 12], [14, 11],[14, 10], [14, 9], [14, 8], [15, 12],
                                                 [15, 11], [15, 10], [15, 9], [15, 8],[16, 12], [16, 11], [16, 10],
                                                 [16, 9], [16, 8], [17, 8]], [], [], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -3:
                        level_scene = 3
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 8], [1, 12], [1, 11], [1, 10], [1, 9], [2, 12], [2, 11], [2, 10],
                                                 [2, 9], [2, 8], [3, 12], [3, 11], [3, 10],[3, 9], [3, 8], [4, 12],
                                                 [4, 11], [4, 10], [4, 9], [4, 8], [7, 12], [7, 11], [7, 10], [7, 9],
                                                 [7, 8], [7, 7], [10, 12], [10, 11], [10, 10], [10, 9], [10, 8], [10, 7], [10, 6],
                                                 [12, 12],[12, 11],[12, 10],[12, 9], [12, 8], [12, 7], [12, 6], [12, 5],
                                                 [14, 12], [14, 11], [14, 10], [14, 9], [14, 8], [14, 7], [14, 6], [14, 5],
                                                 [14, 4], [15, 12], [15, 11], [15, 10], [15, 9], [15, 8], [15, 7], [15, 6],
                                                 [15, 5], [15, 4], [16, 12], [16, 11], [16, 10], [16, 9], [16, 8], [16, 7],
                                                 [16, 6], [16, 5], [16, 4], [17, 4]], [], [], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -4:
                        level_scene = 4
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 4], [1, 12], [1, 11], [1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5],
                                                 [2, 12], [2, 11], [2, 10], [2, 9], [2, 8], [2, 7], [2, 6], [2, 5], [2, 4],
                                                 [3, 12], [3, 11], [3, 10], [3, 9], [3, 8], [3, 7], [3, 6], [3, 5], [3, 4],
                                                 [4, 12], [4, 11], [4, 10], [4, 9], [5, 12], [5, 11], [5, 10], [5, 9],
                                                 [6, 12],  [6, 11], [6, 10], [6, 9], [7, 12], [7, 11], [7, 10], [7, 9],
                                                 [8, 12], [8, 11], [8, 10], [8, 9], [9, 12], [9, 11], [9, 10], [9, 9],
                                                 [10, 12], [10, 11], [10, 10], [10, 9], [11, 12], [11, 11], [11, 10], [11, 9],
                                                 [12, 12], [12, 11], [12, 10], [12, 9], [13, 12], [13, 11], [13, 10], [13, 9],
                                                 [14, 12], [14, 11], [14, 10], [14, 9], [15, 12], [15, 11], [15, 10], [15, 9],
                                                 [16, 12], [16, 11], [16, 10], [16, 9], [17, 9]], [[4, 9], [5, 9], [6, 9], [7, 9]],
                                                [[13, 9]], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -5:
                        level_scene = 5
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 9], [1, 12], [1, 11], [1, 10], [2, 12], [2, 11], [2, 10], [2, 9], [3, 12],
                                                 [3, 11], [3, 10], [3, 9], [4, 12], [4, 11], [4, 10], [4, 9], [5, 12],
                                                 [5, 11], [5, 10], [5, 9], [6, 9], [10, 12]], [[5, 9]], [[6, 9]], [10, 12], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    if level_scene == 1:
                        builder.enemy_list[0].move(5, 750, 400)

                    elif level_scene == 4:
                        builder.enemy_list[0].move(5, 750, 350)

                    elif level_scene == 5:
                        builder.enemy_list[0].move(5, 750, 300)

                if level == 4:
                    background_1.background_img = pygame.image.load(RED_SKY_SPRITE)
                    background_2.background_img = pygame.image.load(RED_SKY_SPRITE)

                    physics.background_moving(background_1, background_2)

                    if level_scene == -1:
                        level_scene = 1
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 8], [2, 8], [3, 8], [4, 8], [7, 8], [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8],
                                                 [14, 8], [15, 8], [16, 8], [17, 8]],
                                                 [[4, 8]], [[9, 8]], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -2:
                        level_scene = 2
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 8], [2, 8], [3, 8], [5, 10], [6, 10], [10, 8], [11, 8],
                                                 [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8]], [[5, 10], [14, 8]],
                                                [[6, 10], [13, 8]], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -3:
                        level_scene = 3
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 8], [2, 8], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3],
                                                 [9, 3], [10, 3], [11, 3], [12, 3], [13, 3], [14, 3], [15, 3], [16, 3], [17, 3]],
                                                 [[4, 7], [6, 5], [8, 3]], [], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -4:
                        level_scene = 4
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 3], [2, 3], [3, 3], [7, 3], [7, 10], [8, 10], [9, 10], [10, 10], [11, 10],
                                                 [12, 10], [8, 3], [9, 3], [10, 3], [11, 3], [16, 12], [17, 12]],
                                                 [[7, 3],[8, 3], [9, 3], [10, 3], [11, 3], [12, 10]], [[11, 10]], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -5:
                        level_scene = 5
                        builder = WorldBuilding(PLANK_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12],
                                                 [8, 12], [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [14, 12],
                                                 [15, 12], [16, 12], [17, 12]], [], [[7, 12], [9, 12]], [16, 12], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    if level_scene == 1:
                        builder.enemy_list[0].move(3, 450, 200)

                    elif level_scene == 2:
                        builder.enemy_list[0].move(5, 450, 250)
                        builder.enemy_list[1].move(5, 800, 500)

                    elif level_scene == 4:
                        builder.enemy_list[0].move(5, 500, 300)

                    elif level_scene == 5:
                        builder.enemy_list[0].move(5, 350, 100)
                        builder.enemy_list[1].move(5, 750, 400)

                if level == 5:
                    background_1.background_img = pygame.image.load(SPACE_SPRITE)
                    background_2.background_img = pygame.image.load(SPACE_SPRITE)

                    physics.background_moving(background_1, background_2)

                    if level_scene == -1:
                        level_scene = 1
                        builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12],
                                                 [8, 12], [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [14, 12],
                                                 [15, 12], [16, 12], [17, 12]],
                                                 [[5, 12], [7, 12], [9, 12], [11, 12], [13, 12], [15, 12]], [], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -2:
                        level_scene = 2
                        builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 9], [8, 9],
                                                 [9, 9], [10, 9], [11, 6], [12, 6], [13, 6], [14, 6], [16, 12], [17, 12]],
                                                [[10, 9]], [[14, 6]], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -3:
                        level_scene = 3
                        builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12],
                                                 [8, 12], [9, 12], [10, 12], [15, 12], [16, 12], [17, 12]],
                                                 [[6, 12], [7, 12]], [], [], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    elif level_scene == -4:
                        level_scene = 4
                        builder = WorldBuilding(GRASS_SPRITE, SPIKE_SPRITE, ENEMY_SPRITE, FLAG_SPRITE,
                                                [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [5, 11], [5, 10], [5, 9],
                                                 [6, 12], [6, 11], [6, 10], [6, 9], [7, 12], [7, 11], [7, 10], [7, 9],
                                                 [7, 8], [7, 7], [7, 6], [8, 12], [8, 11], [8, 10], [8, 9],
                                                 [8, 8], [8, 7], [8, 6],
                                                 [16, 6], [17, 12], [9, 6]], [[7, 3],[8, 3], [9, 3],
                                                 [10, 3], [11, 3], [12, 10]], [[11, 10]], [16, 6], USER_SCREEN)
                        physics.update_builder(builder.get_tiles(), builder.get_spikes(), builder.get_enemies(),
                                               builder.get_flag())

                    if level_scene == 2:
                        builder.enemy_list[0].move(3, 650, 500)

                    if level_scene == 4:
                        if builder.tiles_list[-1].rect.left == builder.tiles_list[25].rect.right:
                            tile_x_vel = 3

                        if builder.tiles_list[-1].rect.right == builder.tiles_list[26].rect.left:
                            tile_x_vel = -3

                        builder.tiles_list[-1].rect.x += tile_x_vel

                # draw backgrounds
                background_1.draw()
                background_2.draw()

                # load gravity for player
                physics.gravity()

                # all necessary controls
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d: # if d held down, move right
                            physics.move_right = True
                            physics.move_left = False

                        if event.key == pygame.K_a: # if a held down, move left
                            physics.move_left = True
                            physics.move_right = False

                        if event.key == pygame.K_SPACE: # if space pressed, jump
                            if player.y_vel == 0.75:
                                physics.player.y_vel -= 15
                                jump_sound.play()

                        if event.key == pygame.K_e: # if e pressed and at flag, go to next level
                            if builder.flag != None:
                                if pygame.Rect(player.rect).colliderect(builder.flag):
                                    if level == 5:
                                        game = False
                                        you_win = True
                                        level = 0
                                        win_sound.play()

                                    else:
                                        next_level.play()

                                    level += 1
                                    level_scene = -1
                                    player_health = 3
                                    player.rect.x = 100
                                    player.rect.y = 240

                    if event.type == pygame.KEYUP: # if stopped holding down, stop movement for direction
                        if event.key == pygame.K_d:
                            physics.move_right = False

                        if event.key == pygame.K_a:
                            physics.move_left = False

                    if event.type == pygame.QUIT:
                            pygame.quit()
                # if player collidiing with flag, send necessary text to guide them
                if builder.flag != None:
                    if pygame.Rect(player.rect).colliderect(builder.flag):
                        press_e_text.draw()

                # if moving left, x-velocity is negative
                if physics.move_left == True:
                    physics.player.x_vel = -5

                # if moving right, x-velocity is positive
                if physics.move_right == True:
                    physics.player.x_vel = 5

                # load player collision to generate normal force
                physics.collision()

                # if colliding with spikes, lose health and back to start of level scene
                for spike in physics.spikes_list:
                    if pygame.Rect(player.rect).colliderect(spike.rect):
                        player.rect.left = 0
                        player.rect.bottom = physics.tiles_list[0].rect.top - 30

                        if player_health != 1:
                            health_loss_sound.play()

                        player_health -= 1

                # if colliding with enemy, lose health and back to start of level scene
                for enemy in physics.enemy_list:
                    if pygame.Rect(player.rect).colliderect(enemy.rect):
                        player.rect.left = 0
                        player.rect.bottom = physics.tiles_list[0].rect.top - 30

                        if player_health != 1:
                            health_loss_sound.play()

                        player_health -= 1

                # if player over the right side of screen, then go to next level scene
                if player.rect.top >= 600:
                    player.rect.left = 0
                    player.rect.bottom = physics.tiles_list[0].rect.top - 30

                    if player_health != 1:
                        health_loss_sound.play()

                    player_health -= 1

                # collision for if player goes to the very left of screen
                if level_scene == 1 and (player.rect.left <= 0 and physics.move_left == True):
                    player.x_vel = 0

                # collision for if player goes to the very right of screen
                if level_scene == max_level_scene[level-1] and (player.rect.right >= 800 and physics.move_right == True):
                    player.x_vel = 0

                # if player is to the right of screen and its not the first level scene, go to next level scene
                if player.rect.left >= 800:
                        if level_scene != max_level_scene[level-1]:
                            level_scene = (level_scene + 1) * -1
                            player.rect.left = 0

                # if player is to the right of screen and its not the last level scene, go to previous level scene
                elif player.rect.right <= 0:
                        if level_scene != 1:
                            level_scene = (level_scene - 1) * -1
                            player.rect.right = 800

                # if player health is 0, go to game over screen
                if player_health == 0:
                    game_over_music.play()
                    game = False
                    game_over = True
                    menu = False

                # if player health is 3, load image
                if player_health == 3:
                    heart_3_img = pygame.image.load(HEART_3)
                    heart_3_img = pygame.transform.scale(heart_3_img, (
                        heart_3_img.get_width() * 3, heart_3_img.get_height() * 3))

                    USER_SCREEN.blit(heart_3_img, (0, 0))

                if player_health == 2:
                    heart_2_img = pygame.image.load(HEART_2)
                    heart_2_img = pygame.transform.scale(heart_2_img, (
                        heart_2_img.get_width() * 3, heart_2_img.get_height() * 3))

                    USER_SCREEN.blit(heart_2_img, (0, 0))

                if player_health == 1:
                    heart_1_img = pygame.image.load(HEART_1)
                    heart_1_img = pygame.transform.scale(heart_1_img, (
                        heart_1_img.get_width() * 3, heart_1_img.get_height() * 3))

                    USER_SCREEN.blit(heart_1_img, (0, 0))

                # if moving right/left/idle, load necessary sprite for player
                if physics.move_right == True:
                    player.update_img(PLAYER_RIGHT_SPRITE)

                elif physics.move_left == True:
                    player.update_img(PLAYER_LEFT_SPRITE)

                elif physics.move_left == False and physics.move_left == False == 0:
                    player.update_img(PLAYER_IDLE_SPRITE)

                # load player movement
                physics.camera_movement()

                # draw all objects
                player.draw()
                builder.draw_tiles()
                builder.draw_spikes()
                builder.draw_enemies()
                builder.draw_flag()

                if level == 1:
                    level_1_text.draw()
                if level == 2:
                    level_2_text.draw()
                if level == 3:
                    level_3_text.draw()
                if level == 4:
                    level_4_text.draw()
                if level == 5:
                    level_5_text.draw()

        # update pygame
        pygame.display.update()



