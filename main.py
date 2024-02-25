import pygame
from pygame.locals import *
import math

class Tile:
    def __init__(self, x, y, size, color=(0, 0, 255), hidden=False):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.hidden = hidden

    def display(self, screen):
        if not self.hidden:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def onCollision(self, screen):
        pass

class Wall(Tile):
    def __init__(self, x, y, size):
        Tile.__init__(self, x, y, size, (65, 128, 255), False)

class Grid:
    def __init__(self, x, y, rows, columns, tile_size):
        self.x = x 
        self.y = y
        self.rows = rows
        self.columns = columns
        self.tile_size = tile_size
        self.tiles = []

        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                tile_x = self.x + j * self.tile_size
                tile_y = self.y + i * self.tile_size
                tile = Tile(tile_x, tile_y, self.tile_size)
                row.append(tile)
            self.tiles.append(row)

    def display(self, screen):
        for row in self.tiles:
            for tile in row:
                tile.display(screen)
    
    def getTile(self, x, y):
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
        # Checks if input is in a perpendicular direction, and if entity is in the center of grid detector
        center_of_tile_x = (self.x // self.grid.tile_size) * self.grid.tile_size + self.grid.tile_size // 2
        center_of_tile_y = (self.y // self.grid.tile_size) * self.grid.tile_size + self.grid.tile_size // 2
        if (self.input_x_direction, self.input_y_direction) != (self.x_direction, self.y_direction) and (self.input_x_direction, self.input_y_direction) != (-self.x_direction, -self.y_direction) and (center_of_tile_x + self.center_of_tile_detector_length) > self.x and (center_of_tile_x - self.center_of_tile_detector_length) < self.x and (center_of_tile_y + self.center_of_tile_detector_length) > self.y and (center_of_tile_y - self.center_of_tile_detector_length) < self.y:
            # teleport to the center of the current tile
            self.x = center_of_tile_x
            self.y = center_of_tile_y
            self.x_direction, self.y_direction = self.input_x_direction, self.input_y_direction
        elif (self.input_x_direction, self.input_y_direction) == (-self.x_direction, -self.y_direction):
            self.x_direction, self.y_direction = self.input_x_direction, self.input_y_direction

        self.x += self.x_direction * self.speed
        self.y += self.y_direction * self.speed

    def display(self, screen):
        pygame.draw.rect(screen, self.color, (self.x + (self.grid.tile_size // 2), self.y + (self.grid.tile_size // 2), self.grid.tile_size, self.grid.tile_size))

# game setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


rows = 36
columns = 28
tile_size = 16
grid = Grid(0, 0, rows, columns, tile_size)
pacman = MovingEntity(grid, 200, 200, 1.46, ("yellow"))

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
