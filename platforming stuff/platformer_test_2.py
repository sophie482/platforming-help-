import pygame

# global constants

# Colours
colourrr = (168, 50, 50)
colourrr2 = (50, 135, 168)
colourrr3 = (185, 185, 190)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colourrr4 = (50, 100, 150)

# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    # bar at the bottom

    # functions
    def __init__(self):
        # constructor
        
        # call parent's constructor
        super().__init__()

        # create image of block and fill with colour
        width = 40
        height = 60
        self.image  = pygame.Surface([width, height])
        self.image.fill(colourrr)

        # set a reference to the image rect
        self.rect = self.image.get_rect()

        # set speed vector of player
        self.change_x = 0
        self.change_y = 0 

        # list of sprites we can bump against
        self.level = None
    
    def update(self):
        # gravity 
        self.calc_grav()

        # move left/right
        self.rect.x += self.change_x

        # see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list: 
            # if we are moving right, set right side to left side of item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0: 
                #otherwise if we are moving left do the opposite
                self.rect.left = block.rect.right
        
        # move up/down
        self.rect.y += self.change_y

        # check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list: 

            # reset our position based 
            if self.change_y > 0: 
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

                # stop vertical movement
                self.change_y = 0
        
    def calc_grav(self):
        # calculate effect of gravity
        if self.change_y == 0:
            self.change_y = 1
        else: 
            self.change_y += .35

        # see if we are on the ground
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0: 
            self.change_y = 0 
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self): 
        # called when the user hits jump button

        #move down a bit and see if there is a platform below us
        #move down 2 pixels
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False) 
        self.rect.y -= 2

        # if it is ok to jump, set speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # player-controlled movement: 
    def go_left(self):
        # called when user hits left arrow 
        self.change_x = -6
    
    def go_right(self):
        # when user hits right arrow
        self.change_x = 6

    def stop(self): 
        # when user lets go of keyboard
        self.change_x = 0

class Platform(pygame.sprite.Sprite): 
    # platform the user can jump on 

    def __init__(self, width, height):
        # platform constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colourrr2)

        self.rect = self.image.get_rect()

class Level():
    # this is a generic super-class used to define a level

    def __init__(self, player):
        # constructor
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # how far world has gone left/right
        self.world_shift = 0
    
    # update everything on level
    def update(self):
        # update everythinhg in this level
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        # draw everything on level

        screen.fill(colourrr3)

        # draw all sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x): 
        # when the user moves/left right

        # keep track
        self.world_shift += shift_x

        # go through all lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# create platforms for the level
class Level_01(Level):
    # definition for level 1

    def __init__(self, player): 
        # create level 1

        # call parent constuctor
        Level.__init__(self, player)

        self.level_limit = -1000

        # array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
        [210, 70, 200, 400], 
        [210, 70, 600, 300],
        [210, 70, 200, 200], 
        [210, 70, 100, 75],
        [210, 70, 600, 100],
        [210, 70, 750, 200],
        [210, 70, 500, 500],
        [210, 70, 800, 400],
        [210, 70, 1000, 500],
        [210, 70, 1120, 280],
        [210, 70, 1300, 300], 
        [210, 70, 1450, 200],
        [210, 70, 1600, 500],
        [210, 70, 1800, 100],
        [20, SCREEN_HEIGHT, 2100, 0]
        ]

        # go through the array above and add platforms
        for platform in level: 
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

class Level_02(Level):
    def __init__(self, player): 
        
        Level.__init__(self, player)

        self.level_limit = -1000

        level = [[210, 70, 200, 500],
        [210, 70, 200, 300], 
        [210, 50, 600, 300],
        [210, 70, 25, 200], 
        [210, 70, 50, 60],
        [210, 90, 700, 200],
        [120, 50, 850, 400],
        [20, 70, 1000, 100],
        [210, 70, 1100, 300],
        [300, 50, 1200, 175],
        [100, 60, 1600, 100],
        [210, 70, 1300, 500],
        [300, 70, 1700, 400],
        [210, 70, 1700, 200],
        [20, SCREEN_HEIGHT, 2100, 0]
        ]

        for platform in level: 
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

class Level_03(Level):
    # definition for level 1

    def __init__(self, player): 
        Level.__init__(self, player)

        self.level_limit = -1000

        # array with width, height, x, and y of platform
        level = [[210, 70, 100, 200],
        [100, 50, 300, 400],
        [300, 20, 400, 100],
        [200, 90, 600, 500],
        [100, 50, 900, 450],
        [150, 20, 1100, 350],
        [20, 150, 1300, 300],
        [250, 50, 1500, 200],
        [100, 20, 1800, 100],
        [20, SCREEN_HEIGHT, 2100, 0]]

        # go through the array above and add platforms
        for platform in level: 
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

class Level_04(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.level_limit = -1000

        level = []

def Text(coordinates, words):
      font = pygame.font.SysFont('Verdana', 50, True, False) 
      text = font.render(words, True, WHITE)
      screen.fill(BLACK)
      screen.blit(text, [coordinates])
      pygame.display.update()
      pygame.time.delay(1500)
      main()

def main():
    pygame.init()
    

    # set height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("platformer test")

    # create player
    player = Player()

    # create all levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))

    # set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 100
    player.rect.y = 75
    # player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # loop until user clicks the close button
    done = False

    # used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # main program loop
    while not done: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP: 
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0: 
                    player.stop()

        # update player
        active_sprite_list.update()

        # update items in the level
        current_level.update()

        font = pygame.font.SysFont('Verdana', 25, True, False) 
        text = font.render("LEVEL " + str(current_level_no + 1), True, colourrr4)
        screen.blit(text, [0, 0])
        pygame.display.update()

        # if the player gets near the right side, shift left
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # opposite for left side
        if player.rect.left <= 120: 
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        #if player gets to end of level, go to next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            if current_level_no + 1 > 3:
                font = pygame.font.SysFont('Verdana', 50, True, False) 
                text = font.render("YOU WON", True, WHITE)
                screen.fill(BLACK)
                screen.blit(text, [215, 250])
                pygame.display.update()
                pygame.time.delay(1500)
                main()

        # if player falls to the bottom, game over
        if player.rect.bottom == SCREEN_HEIGHT: 
            font = pygame.font.SysFont('Verdana', 50, True, False) 
            text = font.render("GAME OVER", True, WHITE)
            screen.fill(BLACK)
            screen.blit(text, [215, 250])
            pygame.display.update()
            pygame.time.delay(1500)
            main()

        #draw
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        # all code to draw should go above this comment

        # limit to 60 FPS
        clock.tick(60)

        # update screen
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__": 
    main()