import pygame					#- importing the graphics module
import random
import math
import sys

##== INITIAL SETUP
#- Initializing Pygame
pygame.init()						#- initialize the module

#- Activate graphical window
WindowWidth = 800						#- fixed width and height of the game window
WindowHeight = 600
Window = pygame.display.set_mode ([WindowWidth, WindowHeight])	#- activate the screen
pygame.display.set_caption ("Pygame template")		#- window title

#- Setup timing
Clock = pygame.time.Clock()				#- initialize the clock module

#- Initializing variable settings
Fps = 60				#- game ticks per second
SizeFloor = 1
gravity = 10.0
surface1 = pygame.image.load ("moonlander.xcf")	#- image from file [pygame.Surface]
PlayerSpawnLocationX = 100              #- Setting up variables
PlayerSpawnLocationY = 100                  #- Setting up variables
BasicCycle = True				#- executing the main cycle

class Ground:
  def __init__(self):
      self.TerrainL = [[0,600],[0,450],[100,450],[175,500],[225,500],[250,300],[300,300],[475,500],[700,550],[800,150],[800,600]]
  def draw(self, Window):
    pygame.draw.polygon (Window, [160,80,0], self.TerrainL)
    
  
class Floor:
  def __init__(self, FloorSpawnLocationY, FloorSpawnLocationX, sizex, sizey):
    self.FloorSpawnLocationX = FloorSpawnLocationX  #- Floor X position
    self.FloorSpawnLocationY = FloorSpawnLocationY  #- Floor Y position
    self.sizex = sizex  #- Floor width
    self.sizey = sizey  #- Floor height
    self.Surface2 = pygame.Surface([self.sizex, self.sizey], pygame.SRCALPHA, 32)  #- Create surface for the Floor
    self.Surface2.fill([0, 200, 200])  #- Fill the Floor with a color
    pygame.draw.rect(self.Surface2, [255, 0, 0], [self.FloorSpawnLocationX, self.FloorSpawnLocationY, self.sizex, self.sizey], 100)  #- Draw a red rectangle (the Floor)
    self.FloorRect2 = self.Surface2.get_rect(x=FloorSpawnLocationX, y=FloorSpawnLocationY)  #- Set the position of the Floor

  def draw(self, Window):
    """ Drawing the Floor into the window """
    Window.blit(self.Surface2, self.FloorRect2)  #- Blit (draw) the Floor on the screen  

class Player:
  def __init__ (self, centerY, centerX, Health):
    self.Health = Health   
    self.centerX = centerX   
    self.centerY = centerY
    self.size = 20   
    self.speedX = 0
    self.speedY = 1
    self.__surface = surface1
    self.angle = 0
    self.TransSurf = pygame.transform.rotate (self.__surface ,-self.angle)		#- rotate image along lander tilt
    self.TransRect = self.TransSurf.get_rect (center=(self.centerX,self.centerY))		#- lander location of rotated image
    self.thrustVariable = 20

    
  def thrust (self):
    """ Activate lander main engine. """
    self.speedX += Player1.thrustVariable / Fps * math.sin (self.angle/180*math.pi)	#- adjust speed (according to FPS)
    self.speedY -= Player1.thrustVariable / Fps * math.cos (self.angle/180*math.pi)
  def update (self):
    """ Execute game logical step. """
    self.centerX += self.speedX / Fps		#- adjust lander position by speed (according to FPS)
    self.centerY += self.speedY / Fps
    self.speedY +=  gravity / Fps		#- adjust lander speed by gravity (according to FPS)
    print("x = ",Player1.centerX," y = ",Player1.centerY)
  def turn (self, leftOrRight):
    self.angle = self.angle + leftOrRight
  def draw (self, Window):
    """ Draw image into window.
        args:
          Window - target surface [pygame.Surface] """
    self.TransSurf = pygame.transform.rotate (self.__surface ,-self.angle)		#- rotate image along lander tilt
    self.TransRect = self.TransSurf.get_rect (center=(self.centerX,self.centerY))		#- lander location of rotated image
    Window.blit (self.TransSurf, self.TransRect)						#- paint image
    
Player1 = Player(PlayerSpawnLocationX, PlayerSpawnLocationY, 1000) #- Note: 'Player1' is now created from the 'Player' class
Floor1 = Floor(random.randint(1, WindowHeight-100), random.randint(1, WindowWidth-100), 40, 5)  #- Initialize Floor1  
Ground1 = Ground() 
  
##== MAIN GAME CYCLE
while BasicCycle:

#- Handling user input
  for event in pygame.event.get():			#- handle input events (keyboard, mouse)
    if event.type == pygame.QUIT:			#--  exit program if requested (Alt+F4, close button)
      BasicCycle = False

#- Display
  Window.fill ([0,0,0])					#- fill the window with black

#  for i in range(1,100):
#    Floor1.FloorRect2.x = Floor1.FloorRect2.x + i
#    Floor1.draw(Window)  
#    pygame.draw.rect (Window, [255,128,0], [0+i,500+a[i],10,10], 0)
  
     
  Keyboard = pygame.key.get_pressed()			#- get the state of the keyboard
  
  if Keyboard[pygame.K_UP]:				#- if UP key is pressed
    Player1.thrust()  
     
  if Keyboard[pygame.K_RIGHT]:				#- if RIGHT key is pressed
    Player1.turn(0.4)
  if Keyboard[pygame.K_LEFT]:				#- if LEFT key is pressed
    Player1.turn(-0.4)

  if Player1.TransRect.colliderect(Floor1.FloorRect2):
      if Player1.speedY > 10 and Player1.speedY > 0:
        print("Crash")
        print("You hit the ground, start over!")
                                       
      else:
        if Player1.speedX < 3 and Player1.speedX > 0:
          Player1.speedY = 0  
          Player1.speedX = 0
          print("You Landed!")
        else:
          print("Crash")
          print("You hit the ground, start over!")

   
  Ground1.draw(Window)  
  print("Speed Y:",Player1.speedY ," ,Speed X:",Player1.speedX)  
  Player1.update()		#- process the lander  
  Player1.draw(Window)
  Floor1.draw(Window)  
  pygame.display.flip()					#- perform rendering from memory to screen

#- Time delay
  Clock.tick (Fps)					#- delay game flow according to set FPS
