import pygame
from pygame.locals import *
import math

class Tile:
    def __init__(self, x, y, size, color=(10, 10, 10), hidden=False):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.hidden = hidden

    def display(self, screen):
        if not self.hidden:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def on_collision(self, screen):
        pass

class Wall(Tile):
    def __init__(self, x, y, size):
        Tile.__init__(self, x, y, size, (0, 0, 255), False)

class Grid:
    def __init__(self, x, y, rows, columns, tile_size, tile_map):
        self.x = x 
        self.y = y
        self.rows = rows
        self.columns = columns
        self.tile_size = tile_size
        self.tile_map = tile_map
        self.tiles = []

        if len(tile_map) != self.rows * self.columns:
            print("Error: Tile map of length", len(tile_map), "does not match grid size of", self.rows * self.columns)
            exit()
        
        character = 0
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                tile_x = self.x + j * self.tile_size
                tile_y = self.y + i * self.tile_size
                row.append(self.__convert_char_to_tile(self.tile_map[character], tile_x, tile_y))
                character += 1
            self.tiles.append(row)

    def __convert_char_to_tile(self, character, x, y):
        tile = None
        match character:
            case 'X':
                tile = Tile(x, y, self.tile_size)
            case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
                tile = Wall(x, y, self.tile_size)
            case '.':
                tile = Tile(x, y, self.tile_size)
                # pellet, when implemented
            case 'p':
                tile = Tile(x, y, self.tile_size)
                # power pellet, when implemented
            case '=':
                # ghost house door, change when implemented
                tile = Wall(x, y, self.tile_size)
            case 't':
                # teleporter, when implemented
                tile = Wall(x, y, self.tile_size)
            case 'f':
                # fruit, when implemented
                tile = Tile(x, y, self.tile_size)
        if tile == None:
            print("Error: Invalid tile map at character:", character)
            exit()
        return tile

    def display(self, screen):
        for row in self.tiles:
            for tile in row:
                tile.display(screen)
    
    def get_tile(self, x, y):
        x = int(x)
        y = int(y)
        # array starts at 0, (x, y) start at 1
        # also, x + y are swapped in tile array
        return self.tiles[y + 1][x + 1]

class MovingEntity:
    def __init__(self, grid, x, y, speed, color):
        self.grid = grid
        self.x = x
        self.y = y
        self.speed = speed
        self.x_direction = -1
        self.y_direction = 0
        self.input_x_direction = -1
        self.input_y_direction = 0
        self.center_of_tile_detector_length = 1
        self.color = color
        
    def update(self):
        center_of_tile_x = (self.x // self.grid.tile_size) * self.grid.tile_size + self.grid.tile_size // 2
        center_of_tile_y = (self.y // self.grid.tile_size) * self.grid.tile_size + self.grid.tile_size // 2
        
        # if entity wants to turn, wait until it is in the center of the tile, then turn
        if (self.input_x_direction, self.input_y_direction) != (self.x_direction, self.y_direction) and (self.input_x_direction, self.input_y_direction) != (-self.x_direction, -self.y_direction) and (center_of_tile_x + self.center_of_tile_detector_length) > self.x and (center_of_tile_x - self.center_of_tile_detector_length) < self.x and (center_of_tile_y + self.center_of_tile_detector_length) > self.y and (center_of_tile_y - self.center_of_tile_detector_length) < self.y:
            # teleport to the center of the current tile
            self.x = center_of_tile_x
            self.y = center_of_tile_y
            # change direction only if entity will be able to move in that direction
            if not self.__movementProhibited(self.input_x_direction, self.input_y_direction):
                self.x_direction, self.y_direction = self.input_x_direction, self.input_y_direction
        # if entity wants to turn around, turn around immediately
        elif (self.input_x_direction, self.input_y_direction) == (-self.x_direction, -self.y_direction):
            self.x_direction, self.y_direction = self.input_x_direction, self.input_y_direction

        if self.__movementProhibited(self.x_direction, self.y_direction):
            self.x = center_of_tile_x
            self.y = center_of_tile_y
        else:
            self.x += self.x_direction * self.speed
            self.y += self.y_direction * self.speed

    def display(self, screen):
        pygame.draw.rect(screen, self.color, (self.x + (self.grid.tile_size // 2), self.y + (self.grid.tile_size // 2), self.grid.tile_size, self.grid.tile_size))

    def __movementProhibited(self, x_dir, y_dir):
        x = self.x // self.grid.tile_size
        y = self.y // self.grid.tile_size
        # check the next tile
        nextTile = self.grid.get_tile(x + x_dir, y + y_dir)
        return isinstance(nextTile, Wall)

# game setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

rows = 36
columns = 28
tile_size = 16
# '\' ignores newline
tile_map = """\
XXXXXXXXXXXXXXXXXXXXXXXXXXXX\
XXXXXXXXXXXXXXXXXXXXXXXXXXXX\
XXXXXXXXXXXXXXXXXXXXXXXXXXXX\
0111111111111781111111111110\
1............33............1\
1.2332.23332.33.23332.2332.1\
1p3XX3.3XXX3.33.3XXX3.3XX3p1\
1.2332.23332.22.23332.2332.1\
1..........................1\
1.2332.22.23333332.22.2332.1\
1.2332.33.23399332.33.2332.1\
1......33....33....33......1\
011116.39332X33X23393.611110\
XXXXX1.39332X22X23393.1XXXXX\
XXXXX1.33XXXXXXXXXX33.1XXXXX\
XXXXX1.33X455==554X33.1XXXXX\
111116.22X5XXXXXX5X22.611111\
tXXXXX.XXX5XXXXXX5XXX.XXXXXt\
111116.22X5XXXXXX5X22.611111\
XXXXX1.33X45555554X33.1XXXXX\
XXXXX1.33XXXXXXXXXX33.1XXXXX\
XXXXX1.33X23333332X33.1XXXXX\
011116.22X23399332X22.611110\
1............33............1\
1.2332.23332.33.23332.2332.1\
1.2393.23332.22.23332.3932.1\
1p..33.......ff.......33..p1\
832.33.22.23333332.22.33.237\
732.22.33.23399332.33.22.238\
1......33....33....33......1\
1.2333399332.33.2339933332.1\
1.2333333332.22.2333333332.1\
1..........................1\
0111111111111111111111111110\
XXXXXXXXXXXXXXXXXXXXXXXXXXXX\
XXXXXXXXXXXXXXXXXXXXXXXXXXXX\
"""
grid = Grid(0, 0, rows, columns, tile_size, tile_map)
pacman = MovingEntity(grid, 200, 408, 1.46, ("yellow"))

# main game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman.input_x_direction = 0
                pacman.input_y_direction = -1
            if event.key == pygame.K_DOWN:
                pacman.input_x_direction = 0
                pacman.input_y_direction = 1
            if event.key == pygame.K_LEFT:
                pacman.input_x_direction = -1
                pacman.input_y_direction = 0
            if event.key == pygame.K_RIGHT:
                pacman.input_x_direction = 1
                pacman.input_y_direction = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))
    grid.display(screen)
    pacman.update()
    pacman.display(screen)
    
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)
    
pygame.quit()
