import pygame
from pygame.locals import *
import math

class Tile:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)

    def display(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

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

class MovingEntity:
    def __init__(self, grid, x, y, speed):
        self.grid = grid
        self.x = x
        self.y = y
        self.speed = speed
        self.direction_x = -1
        self.direction_y = 0
        self.input_direction_x = -1
        self.input_direction_y = 0
     
    def update(self):
        # checks if the input direction is not equal to the current direction or opposite of current direction
        if (self.input_direction_x, self.input_direction_y) != (self.direction_x, self.direction_y) and (self.input_direction_x, self.input_direction_y) != (-self.direction_x, -self.direction_y):
            # teleport to the center of the current tile
            self.x = (self.x // self.grid.tile_size) * self.grid.tile_size + self.grid.tile_size // 2
            self.y = (self.y // self.grid.tile_size) * self.grid.tile_size + self.grid.tile_size // 2
        self.direction_x, self.direction_y = self.input_direction_x, self.input_direction_y
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed

    def display(self, screen):
        pygame.draw.rect(screen, ("yellow"),  (self.x, self.y, self.grid.tile_size, self.grid.tile_size))

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
entity = MovingEntity(grid, 200, 200, 1.46)

# main game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                entity.input_direction_x = 0
                entity.input_direction_y = -1
            if event.key == pygame.K_DOWN:
                entity.input_direction_x = 0
                entity.input_direction_y = 1
            if event.key == pygame.K_LEFT:
                entity.input_direction_x = -1
                entity.input_direction_y = 0
            if event.key == pygame.K_RIGHT:
                entity.input_direction_x = 1
                entity.input_direction_y = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))
    grid.display(screen)
    entity.update()
    entity.display(screen)
    
    print(entity.y)
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)
    
pygame.quit()
