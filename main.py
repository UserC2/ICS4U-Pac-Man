# class Tile:
#   def __init__(self, x, y, size):
#       self.x = x
#       self.y = y
#       self.size = size
#       self.color = color(0, 0, 255)

#   def display(self):
#       fill(self.color)
#       rect(self.x, self.y, self.size, self.size)

# class Grid:
#   def __init__(self, x, y, rows, columns, tile_size):
#       self.x = x  # x position of the grid
#       self.y = y  # y position of the grid
#       self.rows = rows
#       self.columns = columns
#       self.tile_size = tile_size
#       self.tiles = []

#       for i in range(self.rows):
#           row = []
#           for j in range(self.columns):
#               tile_x = self.x + j * self.tile_size
#               tile_y = self.y + i * self.tile_size
#               tile = Tile(tile_x, tile_y, self.tile_size)
#               row.append(tile)
#           self.tiles.append(row)

#   def display(self):
#       for row in self.tiles:
#           for tile in row:
#               tile.display()

# def setup():
#   global grid
#   size(1000, 1000)
#   rows = 36
#   columns = 28
#   tile_size = 20
#   grid = Grid(0, 0, rows, columns, tile_size)

# def draw():
#   background(0)
#   grid.display()