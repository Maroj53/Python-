import pygame                    #- Import the Pygame graphics module
import ctypes

##== INITIAL SETUP
#- Initialize Pygame
pygame.init()                        #- Initialize the module

#- Activate the graphical window
WindowWidth = 1200                        #- Set the width of the game window
WindowHeight = 400                       #- Set the height of the game window
Window = pygame.display.set_mode ([WindowWidth, WindowHeight])    #- Activate the window
pygame.display.set_caption ("Catch game")        #- Set the window title

# Windows API Constants and Functions (ctypes)
user32 = ctypes.windll.user32
hwnd = pygame.display.get_wm_info()['window']
DisplayDefaultSize=pygame.display.get_desktop_sizes

# Function to move window using WinAPI
def move_window(x, y):
    user32.SetWindowPos(hwnd, 0, x, y, 0, 0, 0x0001)

window_x, window_y = 100, 100  # Initial position of the window

#- Prepare the timer
Clock = pygame.time.Clock()                #- Initialize the timing module

#- Initial variable setup
Fps = 60                    #- Set the frames per second to 60
MainLoop = True                #- Main game loop flag, used to keep the game running
i2 = 1
i1 = 1

#- Initial classes setup

Playerspawnlocationx = 10                   #- Set the initial X position for the player spawn
Playerspawnlocationy = 10                   #- Set the initial Y position for the player spawn

# Define the Player class
class Players:
  def __init__(self, centerY, centerX, WalkSpeed, size, Health):
    self.Health = Health  #- Zombie health
    self.centerX = centerX  #- Player's X position
    self.centerY = centerY  #- Player's Y position
    self.WalkSpeed = WalkSpeed  #- Player's walk speed
    self.size = size  #- Player's size
    self.resetspeed = WalkSpeed
    self.Surface2 = pygame.Surface([self.size, self.size], pygame.SRCALPHA, 32)  #- Create surface for the player
    self.Surface2.fill([200, 200, 200])  #- Fill the player with a color
    pygame.draw.circle(self.Surface2, [255, 0, 0], [self.centerX, self.centerY], self.size)  #- Draw a red circle (the player)
    self.PlayerRect2 = self.Surface2.get_rect(x=Playerspawnlocationx, y=Playerspawnlocationy)  #- Set the position of the player
  def draw(self, Window):
    """ Drawing the player into the window """
    Window.blit(self.Surface2, self.PlayerRect2)  #- Blit (draw) the player on the screen

# Initialize the objects for players
Player1 = Players(Playerspawnlocationx, Playerspawnlocationy, 7, 20,700)  #- Initialize Player1



##== MAIN GAME LOOP
while MainLoop:
  #- Handle user input (keyboard events, etc.)
  for event in pygame.event.get():  #- Handle events (like quit)
    if event.type == pygame.QUIT:  #- If the quit event is triggered (e.g., window close button pressed)
      MainLoop = False  #- Exit the main loop and end the game

  # Debug prints to check positions and stamina values
  print("Player coordinates", Player1.PlayerRect2.x, Player1.PlayerRect2.y)  #- Print Player1's X and Y position
  
  #- Drawing
  Window.fill([0, 0, 0])  #- Fill the window with black color (background)

  #- Program function that manages all game logic
  def Program(PlayerClasses1):
    global WindowHeight
    global WindowWidth
    global window_x
    global window_y
    global i1
    global i2


        


 
      
    if PlayerClasses1.PlayerRect2.x <= 0:
        PlayerClasses1.PlayerRect2.x = 0
    if PlayerClasses1.PlayerRect2.x >= WindowWidth - PlayerClasses1.size:
        PlayerClasses1.PlayerRect2.x = WindowWidth - PlayerClasses1.size

    if PlayerClasses1.PlayerRect2.y <= 0:
        PlayerClasses1.PlayerRect2.y = 0
    if PlayerClasses1.PlayerRect2.y >= WindowHeight - PlayerClasses1.size:
        PlayerClasses1.PlayerRect2.y = WindowHeight - PlayerClasses1.size

      
      #Drawing


    PlayerClasses1.draw(Window)  #- Draw Player




    #- Control player movement
    Keyboard = pygame.key.get_pressed()	

    if Keyboard[pygame.K_w]:				#Player movement up
        PlayerClasses1.PlayerRect2.y = PlayerClasses1.PlayerRect2.y - PlayerClasses1.WalkSpeed
    Keyboard = pygame.key.get_pressed()			
    if Keyboard[pygame.K_s]:				#Player movement down
        PlayerClasses1.PlayerRect2.y = PlayerClasses1.PlayerRect2.y + PlayerClasses1.WalkSpeed
    Keyboard = pygame.key.get_pressed()			
    if Keyboard[pygame.K_a]:				#Player movement left
        PlayerClasses1.PlayerRect2.x = PlayerClasses1.PlayerRect2.x - PlayerClasses1.WalkSpeed
    Keyboard = pygame.key.get_pressed()			
    if Keyboard[pygame.K_d]:				#Player movement right
        PlayerClasses1.PlayerRect2.x = PlayerClasses1.PlayerRect2.x + PlayerClasses1.WalkSpeed
        

    if  PlayerClasses1 == Player1:    
        if Keyboard[pygame.K_LSHIFT] and Stamina > 0:                #- if 'Left Shift' key is pressed
            PlayerClasses1.WalkSpeed   = 10
            Stamina = Stamina - 2
        else:
            PlayerClasses1.WalkSpeed = PlayerClasses1.resetspeed

    if PlayerClasses1.PlayerRect2.x <= 0:
        i1 = -1
    if PlayerClasses1.PlayerRect2.x >= WindowWidth - PlayerClasses1.size:
        i1 = 1

    if PlayerClasses1.PlayerRect2.y <= 0:
        i2 = -1
    if PlayerClasses1.PlayerRect2.y >= WindowHeight - PlayerClasses1.size:
        i2 = 1



    window_x, window_y = window_x + i1, window_y + i2  # Move the window by 1 pixel
    move_window(window_x, window_y)  # Move the window

  #- Update the window display

  Program(Player1)  #- Call the game logic



  #- Update the window
  pygame.display.flip()

  #- Control the game framerate
  Clock.tick(Fps)  #- Limit the frame rate to 60 FPS

pygame.quit()  #- Quit Pygame when the game loop ends
