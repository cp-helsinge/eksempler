 # -*- coding: utf-8 -*-



 {'alien1'        : {
    'position': (x,y)
    'boundary'    : (0,0,1000,200),
    'speed'       : 2, # optional
    'direction'   : 180, # optional
    'move_pattern': 'horisontal',# optional
    
  }}, 
      

class Sprite:
  def __init__(
    self, 
    name, 
    rect = False, 
    frame_rate = False,
    loop = -1,
    frame_rect = False
  ):class Sprite:
  pass


class Gameobject:
  def __init__(self, boundry, position, size, speed, direction):
    # Set boundry (Default to screen size)
    if boundary is not None:
      self.boundary = pygame.Rect(boundary)
    else:
      self.boundary = globals.game.rect

    # Place on screen (Default to center of boundry)
    if position is None:
      self.position = (self.boundry.width//2 + self.boundry.x, self.boundry.height//2 + self.boundry.y) 
    else 
      self.position = position
  
    # Set scaled size (Default to real image size)
    if size is None:
      self.size = Alien1.__sprite.size
    else
      self.size = size

    self.rect       = pygame.Rect(self.position, self.size)
    self.speed      = speed
    self.direction  = direction

    self.delete     = False



class Alien1(Gameobject):
  # define alien animation images and sounds
  __image_name = "alien-{index}.png"      # Alien sprite map image file name
  __image_size = (100,50)                 # Image frame size
  __image_bomb_name = 'bomb.png'          # Bomb sprite map image file name
  __image_bomb_size = (40,40)             # Image frame size
  __image_shot_name = 'shot.png'          # Shot sprite map image file name
  __image_shot_size = (8,8)               # Image frame size
  __sound_die_name = 'small_bang.wav'     # Sound to make when dieing
  __sound_bomb_name = 'drop_bomb.wav'     # Sound to make when dropping a bomb
  __sound_shoot_name = 'plop.wav'         # Sound to make when shooting
  
  # Variables to store animations ans sounds (Must only load once)
  __loaded = False
  __sprite = None
  __sprit_bomb = None
  __sprit_shot = None
  __sound_die = None
  __sound_shoot = None

  # Initialize Alien 1 with defaults
  def __init__(self, boundary = None, position = None, size = None, direction = 0, speed = 1):
    # Load animations and sounds
    if not Alien1.__loaded:
      Alien1.__sprite = Sprite(Alien1.__image_name, Alien1.__image_size)
      Alien1.__sprite_bomb = Sprite(Alien1.__image_bomb_name, Alien1.__image_bomb_size)
      Alien1.__sprite_shot = Sprite(Alien1.__image_shot_name, Alien1.__image_shot_size)
    # Inherit gameobject 
    Gameobject.__init__(self, boundry, position, size, speed, direction)

  # Draw on game surface
  def draw(self, surface):
    # Flip image when direction is left
    if self.direction > 0:
      surface.blit(pygame.transform.flip(self.sprite.get_surface(),True,False),self.rect)
    else:  
      surface.blit(self.sprite.get_surface(),self.rect)
    
  # Movement
  def update(self):
    # test if out of boundry
    if common.rect_touch(self.rect, self.boundary):
      # Change to oposite direction
      self.direction = (self.direction + 180) % 360 // 1

    self.rect = common.move_rect(self.rect, self.direction, self.speed, self.boundary)  

  # When hit or hitting something
  def hit(self, object_type, score):
    if object_type == 'shot':
      self.delete = True
      score += 100
