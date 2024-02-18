
class Tile:
  def __init__(self, x, y, size):
      self.x = x
      self.y = y
      self.size = size
      self.color = color(0, 0, 255)

  def display(self):
      fill(self.color)
      rect(self.x, self.y, self.size, self.size)

class Grid:
  def __init__(self, x, y, rows, columns, tile_size):
      self.x = x  # x position of the grid
      self.y = y  # y position of the grid
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

  def display(self):
      for row in self.tiles:
          for tile in row:
              tile.display()

class MovingEntity:
  def __init__(self, grid, start_x, start_y, step_size, move_interval):
      self.grid = grid
      self.x = start_x
      self.y = start_y
      self.target_x = start_x
      self.target_y = start_y
      self.step_size = step_size  # step size for each movement
      self.move_interval = move_interval  # time interval for each movement
      self.current_step = 0  # current step in the movement
      self.is_moving = False  # flag to track if entity is moving
      self.direction = None  # direction of movement

  def set_direction(self, direction):
      self.direction = direction

  def update_movement(self):
      if not self.is_moving:
          if self.direction == 'up' and self.x > 0:
              self.target_x -= 1
              self.is_moving = True
          elif self.direction == 'down' and self.x < self.grid.rows - 1:
              self.target_x += 1
              self.is_moving = True
          elif self.direction == 'left' and self.y > 0:
              self.target_y -= 1
              self.is_moving = True
          elif self.direction == 'right' and self.y < self.grid.columns - 1:
              self.target_y += 1
              self.is_moving = True

      if self.is_moving:
          # calculate the distance to the target position
          dy = self.target_y - self.y
          dx = self.target_x - self.x

          # calculate the magnitude of the distance vector
          distance = sqrt(dx * dx + dy * dy)

          # normalize the distance vector
          if distance > 0:
              dx /= distance
              dy /= distance

          # move the entity by step size towards the target position
          self.x += dx * self.step_size
          self.y += dy * self.step_size

          # check if the entity has reached or passed the target position
          if (dy > 0 and self.y >= self.target_y) or (dy < 0 and self.y <= self.target_y) or (
                  dx > 0 and self.x >= self.target_x) or (dx < 0 and self.x <= self.target_x):
              # go to the target position if passed
              self.x = self.target_x
              self.y = self.target_y
              self.is_moving = False

  def display(self):
      fill(255, 255, 0)  
      rect(self.grid.x + self.y * self.grid.tile_size, self.grid.y + self.x * self.grid.tile_size, self.grid.tile_size, self.grid.tile_size)

def setup():
  global grid, entity
  size(1000, 1000)
  rows = 36
  columns = 28
  tile_size = 20
  grid = Grid(0, 0, rows, columns, tile_size)
  entity = MovingEntity(grid, 0, 0, 0.1, 10)

def draw():
  background(0)
  grid.display()
  entity.update_movement()
  entity.display()

def keyPressed():
  if keyCode == UP:
      entity.set_direction('up')
  elif keyCode == DOWN:
      entity.set_direction('down')
  elif keyCode == LEFT:
      entity.set_direction('left')
  elif keyCode == RIGHT:
      entity.set_direction('right')
    