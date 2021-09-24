import pygame

# global constants

# Colours
colourrr = (168, 50, 50)
colourrr2 = (50, 135, 168)
colourrr3 = (185, 185, 190)

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
        self.level = 0 
    
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

class Level(object):
    # this is a generic super-class used to define a level

    def __init__(self, player):
        # constructor
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # background image
        self.background = None
    
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

# create platforms for the level
class Level_01(Level):
    # definition for level 1

    def __init__(self, player): 
        # create level 1

        # call parent constuctor
        Level.__init__(self, player)

        # array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
        [210, 70, 200, 400], 
        [210, 70, 600, 300],
        [210, 70, 200, 200], 
        [210, 70, 100, 75]]

        # go through the array above and add platforms
        for platform in level: 
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        print(self.platform_list)
        print("UGH")

class Level_02(Level):
    def __init__(self, player): 
        
        Level.__init__(self, player)

        level = [[210, 70, 200, 500],
        [210, 70, 200, 300], 
        [210, 50, 600, 300],
        [210, 70, 25, 200], 
        [210, 70, 100, 225],
        [210, 70, 50, 60]]

        for platform in level: 
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        print(self.platform_list)
        print("hello")

class Level_03(Level):
    # definition for level 1

    def __init__(self, player): 
        Level.__init__(self, player)

        # array with width, height, x, and y of platform
        level = [[210, 70, 100, 200],
        [210, 70, 50, 20], 
        [210, 70, 300, 500],
        [210, 70, 100, 200], 
        [210, 70, 200, 75]]

        # go through the array above and add platforms
        for platform in level: 
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        print(self.platform_list)
        print("UGH2")


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

    # set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
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

        # if the player gets near the right side, shift left
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
        # opposite for left side
        if player.rect.left < 0: 
            player.rect.left = 0 
            
        if player.rect.bottom < 0: 
            if current_level_no == 0:
                current_level_no = 1
                current_level = level_list[current_level_no]
                player.rect.y = SCREEN_HEIGHT
            elif current_level_no == 1: 
                current_level_no = 2
                current_level = level_list[current_level_no]
                player.rect.y = SCREEN_HEIGHT

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # all code to draw should go above this comment

        # update screen
        pygame.display.flip()

        # limit to 60 FPS
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__": 
    main()