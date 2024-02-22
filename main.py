import pygame

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

# game setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


rows = 36
columns = 28
tile_size = 20
grid = Grid(0, 0, rows, columns, tile_size)

# main game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(("purple"))
    grid.display(screen)

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
