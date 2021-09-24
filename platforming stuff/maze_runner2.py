#http://programarcadegames.com/python_examples/f.php?file=maze_runner.py

import pygame

# COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (24, 132, 168)
GREEN = (25, 115, 48)
RED = (163, 34, 24)
PURPLE = (108, 66, 150)
YELLOW = (222, 193, 29)

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, colour):
        # constructor function 

        # call parents constructor
        super().__init__()

        # make a blue wall, of the size in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # top left corner = passed-in location 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Player(pygame.sprite.Sprite): 
    # the bar at the bottom that the player controls

    #speed vector
    change_x = 0
    change_y = 0

    def __init__(self):
        # constructor function

        # parents constructor
        super().__init__()

        # height, width
        width = 15
        height = 15
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)

        # set a reference 
        self.rect = self.image.get_rect()

        # speed vector of player
        self.change_x = 0
        self.change_y = 0

        self.level = None

    def update(self): 
        # move player
        # gravity
        self.calc_grav()

        #move left/right
        self.rect.x += self.change_x

        # test if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # if we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0: 
                self.rect.right = block.rect.left
            else: 
                # if moving left, do the opposite
                self.rect.left = block.rect.right

        # move up/down
        self.rect.y += self.change_y

        #check to see if we hit a wall
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list: 
            # reset position based on top/bottom of object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Room(object): 
    # base class for all rooms

    # each class has walls
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        # constructor
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

class Room1(Room): 
    # all walls in room one
    def __init__(self): 
        super().__init__()
        # make the walls. (x, y, width, height)

        # list of walls
        walls = [[0, 0, 20, 250, WHITE], 
        [0, 350, 20, 250, WHITE], 
        [780, 0, 20, 250, WHITE], 
        [780, 350, 20, 250, WHITE],
        [20, 0, 760, 20, WHITE], 
        [20, 580, 760, 20, WHITE], 
        [390, 50, 20, 500, BLUE]]

        # creat walls, add them to the list
        for item in walls: 
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

class Room2(Room): 
    #all walls in room 2
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED], 
        [0, 350, 20, 250, RED], 
        [780, 0, 20, 250, RED], 
        [780, 350, 20, 250, RED], 
        [20, 0, 760, 20, RED], 
        [20, 580, 760, 20, RED], 
        [190, 50, 20, 500, YELLOW], 
        [590, 50, 20, 500, YELLOW]]

        for item in walls: 
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

class Room3(Room):
    # all walls in room 3

    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, GREEN],
                 [0, 350, 20, 250, GREEN],
                 [780, 0, 20, 250, GREEN],
                 [780, 350, 20, 250, GREEN],
                 [20, 0, 760, 20, GREEN],
                 [20, 580, 760, 20, GREEN]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall) 

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, BLUE)
                self.wall_list.add(wall)
        
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, YELLOW)
            self.wall_list.add(wall)

class Room4(Room):
    # all walls in room 4

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, BLUE],
        [0, 350, 20, 250, BLUE],
        [780, 0, 20, 250, BLUE],
        [780, 350, 20, 250, BLUE],
        [20, 0, 760, 20, BLUE],
        [20, 580, 760, 20, BLUE]]

        for x in range(200, 600, 20):
            for y in range(100, 350, 100):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for item in walls: 
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

class Room5(Room): 
    # all walls in room 5

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
        [0, 350, 20, 250, WHITE], 
        [780, 0, 20, 250, GREEN],
        [780, 350, 20, 250, BLUE],
        [20, 0, 760, 20, YELLOW],
        [20, 580, 760, 20, PURPLE],
        [20, 230, 50, 20, WHITE], #1st opening
        [20, 350, 100, 20, WHITE], #2nd opening
        [140, 50, 20, 500, WHITE],#1st vertical line
        [20, 425, 100, 20, WHITE],
        [20, 500, 100, 20, WHITE], 
        [50, 50, 20, 200, WHITE],
        [100, 100, 60, 20, WHITE],
        [100, 200, 60, 20, WHITE],
        [100, 300, 60, 20, WHITE],
        [200, 290, 200, 20, WHITE],
        [230, 20, 20, 270, WHITE], 
        [250, 300, 20, 150, WHITE]] 

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


def main(): 

    pygame.init()

    # 800 x 600 screen
    screen = pygame.display.set_mode([800, 600])

    # title
    pygame.display.set_caption("god i hope this works")

    # player object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    room = Room4()
    rooms.append(room)
    
    room = Room5()
    rooms.append(room)

    current_room_no = 0 
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done: 

        # if player closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True

            # player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP: 
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN: 
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT: 
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT: 
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP: 
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN: 
                    player.changespeed(0, -5)

        # logic

        player.move(current_room.wall_list) 

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 1:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 3:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 4:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801: 
            if current_room_no == 0: 
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0 
            elif current_room_no == 1: 
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 2: 
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 3: 
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else: 
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0 

        # drawing
        screen.fill(BLACK)

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        # updates screen
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()