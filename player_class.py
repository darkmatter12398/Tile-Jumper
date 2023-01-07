import pygame

# class for player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, player_img, screen, scale=None): # x/y pos, the image of player, screen of pygame, and scale
        pygame.sprite.Sprite.__init__(self)

        self.x = x # necessary velocity of player
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.player_img = pygame.image.load(player_img)
        self.scale = scale

        if scale != None:
            self.player_img = pygame.transform.scale(self.player_img, (self.player_img.get_width() * scale, self.player_img.get_height() * scale))

        self.rect = self.player_img.get_rect()
        self.rect.center = (self.x, self.y)

        self.screen = screen

    # for drawing player
    def draw(self):
        self.screen.blit(self.player_img, self.rect)

    # for updating its image when it's moving right or left
    def update_img(self, img):
        self.player_img = pygame.image.load(img)

        if self.scale != None:
            self.player_img = pygame.transform.scale(self.player_img, (self.player_img.get_width() * self.scale, self.player_img.get_height() * self.scale))

    # getting position (for debugging)
    def get_pos(self):
        return (self.x, self.y)

# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_img, screen, scale=None): # same param as player
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.enemy_img = pygame.image.load(enemy_img)

        if scale != None:
            self.enemy_img = pygame.transform.scale(self.enemy_img, (self.enemy_img.get_width() * scale, self.enemy_img.get_height() * scale))

        self.rect = self.enemy_img.get_rect()
        self.rect.center = (self.x, self.y)

        self.screen = screen

    # movement for enemy (has max x value and min x value
    def move(self, speed, max_x, min_x):
        if self.x_vel == 0:
            self.x_vel = speed

        if self.rect.x <= min_x:
            self.x_vel = speed

        if self.rect.x >= max_x:
            self.x_vel = -1 * (speed)

        self.rect.x += self.x_vel

    # for drawing enemy
    def draw(self):
        self.screen.blit(self.enemy_img, self.rect)

    # for getting pos of enemy (debugging)
    def get_pos(self):
        return (self.x, self.y)

# class for platforms
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, platform_img, screen, gravity, scale_x, scale_y): # x/y pos, image, screen, if it has gravity, x/y scale
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.gravity = gravity
        self.platform_img = pygame.image.load(platform_img)

        self.platform_img = pygame.transform.scale(self.platform_img,
                                               (scale_x, scale_y))

        self.rect = self.platform_img.get_rect()
        self.rect.center = (self.x, self.y)

        self.screen = screen

        self.on_ground = False # for player (if its on the ground on any tile)

    # for drawing platform
    def draw(self):
        self.screen.blit(self.platform_img, self.rect)

    def get_pos(self):
        return (self.x, self.y)

class Flag(pygame.sprite.Sprite):
    def __init__(self, x, y, flag_img, screen, scale=None): # x/y pos, image, pygame screen, scale factor
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.flag_img = pygame.image.load(flag_img)

        if scale != None:
            self.flag_img = pygame.transform.scale(self.flag_img, (self.flag_img.get_width() * scale, self.flag_img.get_height() * scale))

        self.rect = self.flag_img.get_rect()
        self.rect.center = (self.x, self.y)

        self.screen = screen

    # for drawing flag
    def draw(self):
        self.screen.blit(self.flag_img, self.rect)

    # debugging
    def get_pos(self):
        return (self.x, self.y)

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y, spike_img, screen, scale): # x/y pos, image, pygame screen, scale factor
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.spike_img = pygame.image.load(spike_img)

        if scale != None:
            self.spike_img = pygame.transform.scale(self.spike_img, (
            self.spike_img.get_width() * scale, self.spike_img.get_height() * scale))

        self.rect = self.spike_img.get_rect()
        self.rect.center = (self.x, self.y)

        self.screen = screen

    # for drawing spike
    def draw(self):
        self.screen.blit(self.spike_img, self.rect)

    # for debugging
    def get_pos(self):
        return (self.x, self.y)

#class Coin(pygame.sprite.Sprite):
    # def __init__(self, x, y, coin_img, screen, scale):
    #     pygame.sprite.Sprite.__init__(self)
    #
    #     self.x = x
    #     self.y = y
    #     self.coin_img = pygame.image.load(coin_img)
    #
    #     if scale != None:
    #         self.coin_img = pygame.transform.scale(self.coin_img, (
    #         self.coin_img.get_width() * scale, self.coin_img.get_height() * scale))
    #
    #     self.rect = self.coin_img.get_rect()
    #     self.rect.center = (self.x, self.y)
    #
    #     self.screen = screen
    #
    # def draw(self):
    #     self.screen.blit(self.coin_img, self.rect)
    #
    # def get_pos(self):
    #     return (self.x, self.y)

# class for background

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, background_img, screen): # x/y pos, image, pygame screen
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.background_img = pygame.image.load(background_img)

        self.rect = self.background_img.get_rect()
        self.rect.center = (self.x, self.y)

        self.screen = screen

    # for drawing background
    def draw(self):
        self.screen.blit(self.background_img, self.rect)

    # for moving background
    def move(self):
        self.rect.x -= 1

# class for all the physics in the game
class Physics():
    def __init__(self, gravity_factor, term_vel, builder, player): # gravity magnitude, terminal velocity, worldbuilding class, player class
        self.gravity_factor = gravity_factor
        self.term_vel = term_vel
        self.player = player
        self.builder = builder

        # moving player booleans
        self.move_right = False
        self.move_left = False

        # all arrays for all tiles/collision types for player
        self.tiles_list = builder.get_tiles()
        self.spikes_list = builder.get_spikes()
        self.enemy_list = builder.get_enemies()
        self.flag = builder.get_flag()
        self.left_collision = []
        self.right_collision = []
        self.top_collision = []
        self.bottom_collision = []
        self.on_ground_list = []

        # fill collision variables with "False" to initialize
        for i in range(len(self.tiles_list)):
            self.left_collision.append(False)
            self.top_collision.append(False)
            self.right_collision.append(False)
            self.bottom_collision.append(False)
            self.on_ground_list.append(False)

    # to update builder with new world
    def update_builder(self, new_tiles_list, spikes_list, enemy_list, flag):
        self.tiles_list = new_tiles_list
        self.spikes_list = spikes_list
        self.enemy_list = enemy_list
        self.flag = flag
        self.left_collision = []
        self.right_collision = []
        self.top_collision = []
        self.bottom_collision = []
        self.on_ground_list = []

        for i in range(len(self.tiles_list)):
            self.left_collision.append(False)
            self.top_collision.append(False)
            self.right_collision.append(False)
            self.bottom_collision.append(False)
            self.on_ground_list.append(False)

    # to simulate gravity
    def gravity(self):
        self.player.y_vel += self.gravity_factor

        if self.player.y_vel >= self.term_vel:
            self.player.y_vel = self.term_vel

    # to generate player movement
    def camera_movement(self):
        if (self.move_left == False and self.move_right == False):
            self.player.x_vel = 0

        self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    # for simulating normal force collision (WARNING: very complex)
    def collision(self):
        for i in range(len(self.tiles_list)):

            # if player colliding with tile, then detect which side of tile the player is gonna collide with
            if pygame.Rect(self.player.rect).colliderect(self.tiles_list[i].rect):

                # player's right colliding with tile's left
                if self.left_collision[i] == True:
                    while self.player.rect.right > self.tiles_list[i].rect.left: # if player went through tile, then put player outside of tile
                        self.player.rect.x -= 1

                    if self.player.x_vel > 0:
                        self.player.x_vel = 0

                # player's left colliding with tile's right
                if self.right_collision[i] == True:
                    while self.player.rect.left < self.tiles_list[i].rect.right:
                        self.player.rect.x += 1

                    if self.player.x_vel < 0:
                        self.player.x_vel = 0

                # player's bottom colliding with tile's top
                if self.top_collision[i] == True:
                    while self.player.rect.bottom > self.tiles_list[i].rect.top:
                        self.player.rect.y -= 1

                    if self.player.y_vel > 0:
                        self.player.y_vel = 0

                    self.on_ground_list[i] = True

                # player's top colliding with tile's bottom
                if self.bottom_collision[i] == True:
                    while self.player.rect.top > self.tiles_list[i].rect.bottom:
                        self.player.rect.x += 1

                    if self.player.y_vel < 0:
                        self.player.y_vel = 0

            # if player is not colliding, predict which side of the tile he will collide with
            else:
                # if left of player is greater than right of tile, he will collide with right of tile
                if self.player.rect.left >= self.tiles_list[i].rect.right:
                    self.right_collision[i] = True
                    self.left_collision[i] = False
                    self.top_collision[i] = False
                    self.bottom_collision[i] = False

                    if (self.player.rect.left == self.tiles_list[i].rect.right):
                        if (self.player.rect.bottom > self.tiles_list[i].rect.top) and (self.player.rect.top < self.tiles_list[i].rect.bottom):
                            if self.player.x_vel < 0:
                                self.player.x_vel = 0

                    else:
                        self.on_ground_list[i] = False

                # if right of player is less than left of tile, he will collide with left of tile
                if self.player.rect.right <= self.tiles_list[i].rect.left:
                    self.left_collision[i] = True
                    self.right_collision[i] = False
                    self.top_collision[i] = False
                    self.bottom_collision[i] = False

                    if (self.player.rect.right == self.tiles_list[i].rect.left):
                        if (self.player.rect.bottom > self.tiles_list[i].rect.top) and (self.player.rect.top < self.tiles_list[i].rect.bottom):
                            if self.player.x_vel > 0:
                                self.player.x_vel = 0

                    else:
                        self.on_ground_list[i] = False

                # if top of player is greater than bottom of tile, he will collide with bottom of tile
                if self.player.rect.top >= self.tiles_list[i].rect.bottom:  # bug with player top, tile bottom collision
                    self.bottom_collision[i] = True
                    self.left_collision[i] = False
                    self.top_collision[i] = False
                    self.right_collision[i] = False

                    if (self.player.rect.top == self.tiles_list[i].rect.bottom):
                        if (self.player.rect.right > self.tiles_list[i].rect.left) and (self.player.rect.left < self.tiles_list[i].rect.right):
                            if self.player.y_vel < 0:
                                self.player.y_vel = 0

                    else:
                        self.on_ground_list[i] = False

                # if bottom of player is less than top of tile, he will collide with top of tile
                if self.player.rect.bottom <= self.tiles_list[i].rect.top:
                    self.top_collision[i] = True
                    self.left_collision[i] = False
                    self.right_collision[i] = False
                    self.bottom_collision[i] = False

                    if (self.player.rect.bottom == self.tiles_list[i].rect.top):
                        self.on_ground_list[i] = True

                        if (self.player.rect.right > self.tiles_list[i].rect.left) and (self.player.rect.left < self.tiles_list[i].rect.right):
                            if self.player.y_vel > 0:
                                self.player.y_vel = 0

                    else:
                        self.on_ground_list[i] = False

    # for moving the background images
    def background_moving(self, background_1, background_2):
        if background_1.rect.right == 0:
            background_1.rect.x = 800

        if background_2.rect.right == 0:
            background_2.rect.x = 800

        background_1.rect.x -= 1
        background_2.rect.x -= 1

        background_1.draw()
        background_2.draw()

# class for building tiles, spikes, enemies, and ending flag
class WorldBuilding():

    # tile image, spike image, enemy image, flag image, tile template, spike template, enemy template, flag position, pygame screen
    def __init__(self, block, spike_img, enemy_img, flag_img, template, spike_template, enemy_template, flag_pos, screen):
        self.screen = screen
        self.screen_length = 800
        self.screen_height = 600
        self.template = template
        self.spike_template = spike_template
        self.enemy_template = enemy_template
        #self.coin_template = coin_template
        self.flag_pos = flag_pos

        self.block = block
        self.enemy_img = enemy_img
        self.spike_img = spike_img
        self.flag_img = flag_img
        #self.coin_img = coin_img

        # for storing tiles, spikes, enemies, and flag (there can be only 1 flag)
        self.tiles_list = []
        self.spikes_list = []
        self.enemy_list = []
        #self.coin_list = []
        self.flag = None

    # for updating all the tiles in the game
    def update_tiles(self, new_template):
        self.template = new_template

    # for getting the tiles from a template
    def get_tiles(self):
        block_x_pivot = 25
        block_y_pivot = 25

        # detect all coordinates in the tile template, and place according to template
        for coordinates in self.template:
            block_x_pos = 0
            block_y_pos = 0

            for i in range(coordinates[0]): # x coordinate
                if i == 0:
                    block_x_pos += block_x_pivot

                else:
                    block_x_pos += block_x_pivot * 2

            for i in range(coordinates[1]): # y coordinate
                if i == 0:
                    block_y_pos += block_y_pivot

                else:
                    block_y_pos += block_y_pivot * 2

            # produce platform from coordinates given in template
            platform = Platform(block_x_pos, block_y_pos, self.block, self.screen, False, 50, 50)

            self.tiles_list.append(platform) # append platform to list

        return self.tiles_list

    # for getting the spikes from the spike template
    def get_spikes(self):
        # if spike coordinates is same as a coordinate from the tile template,
        # place spike on tile
        for i in range(len(self.template)):
            for j in range(len(self.spike_template)):
                if self.template[i] == self.spike_template[j]:
                    spike = Spike(0, 0, self.spike_img, self.screen, 0.25)

                    spike.rect.bottom = self.tiles_list[i].rect.top
                    spike.rect.centerx = self.tiles_list[i].rect.centerx

                    self.spikes_list.append(spike)

        return self.spikes_list

    # for getting enemies (same as the "get_spikes()" function)
    def get_enemies(self):
        for i in range(len(self.template)):
            for j in range(len(self.enemy_template)):
                if self.template[i] == self.enemy_template[j]:
                    enemy = Enemy(self.tiles_list[i].rect.left + (self.tiles_list[i].rect.width // 2),
                                  self.tiles_list[i].rect.top - (self.tiles_list[i].rect.height // 2), self.enemy_img, self.screen, 2)

                    self.enemy_list.append(enemy)

        return self.enemy_list

    # def get_coins(self):
    #     coin_x_pivot = 25
    #     coin_y_pivot = 25
    #
    #     for coordinates in self.template:
    #         coin_x_pos = 0
    #         coin_y_pos = 0
    #
    #         for i in range(coordinates[0]):
    #             if i == 0:
    #                 coin_x_pos += coin_x_pivot
    #
    #             else:
    #                 coin_x_pos += coin_x_pivot * 2
    #
    #         for i in range(coordinates[1]):
    #             if i == 0:
    #                 coin_y_pos += coin_y_pivot
    #
    #             else:
    #                 coin_y_pos += coin_y_pivot * 2
    #
    #         coin = Coin(coin_x_pos, coin_y_pos, self.coin_img, self.screen)
    #         self.tiles_list.append(coin)

        # return self.tiles_list

    # for getting the flag

    # for getting flag
    def get_flag(self):
        # if flag coordinates are the same as a tile,
        # then place it on the tile
        for i in range(len(self.template)):
            if self.template[i] == self.flag_pos:
                self.flag = Flag(0, 0, self.flag_img, self.screen)

                self.flag.rect.bottom = self.tiles_list[i].rect.top
                self.flag.rect.centerx = self.tiles_list[i].rect.centerx

                return self.flag

    # for drawing all tiles from tiles list
    def draw_tiles(self):
        for tile in self.tiles_list:
            tile.draw()

    # for drawing spikes from spike list
    def draw_spikes(self):
        for spike in self.spikes_list:
            spike.draw()

    # for drawing enemies from enemies list
    def draw_enemies(self):
        for enemy in self.enemy_list:
            enemy.draw()

    # for drawing flag from flag list
    def draw_flag(self):
        if self.flag != None:
            self.flag.draw()

# class for creating buttons (and text)
# same as some of the other classes
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, button_img, screen, scale=None):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.button_img = pygame.image.load(button_img)

        if scale != None:
            self.button_img = pygame.transform.scale(self.button_img, (self.button_img.get_width() * scale, self.button_img.get_height() * scale))

        self.rect = self.button_img.get_rect()
        self.rect.center = (self.x, self.y)

        self.screen = screen

    # for detecting if cursor hovers over button, and if we want said button to have collision
    def button_collision(self):
        if pygame.Rect(self.rect).collidepoint(pygame.mouse.get_pos()):
            return True

        else:
            return False

    def draw(self):
        self.screen.blit(self.button_img, self.rect)

    def get_pos(self):
        return (self.x, self.y)
