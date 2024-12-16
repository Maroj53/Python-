import pygame                    #- Import the module for graphics
import random

##== INITIAL SETUP
#- Initialize Pygame
pygame.init()                        #- Initialize the modules

#- Activate the graphical window
WindowWidth = 800                    #- Fixed width and height of the game window
WindowHeight = 600
Window = pygame.display.set_mode([WindowWidth, WindowHeight])    #- Activate the screen
pygame.display.set_caption("Pygame Template")        #- Window title

#- Prepare the clock for timing
Clock = pygame.time.Clock()                #- Initialize the time module

Playerspawnlocationx = 100              #- Setting up variables
Playerspawnlocationy = 100                  #- Setting up variables

class Floor:
    def __init__(self, Floorspawnlocationy, Floorspawnlocationx, sizex, sizey):
        self.Floorspawnlocationx = Floorspawnlocationx  #- Floor X position
        self.Floorspawnlocationy = Floorspawnlocationy  #- Floor Y position
        self.sizex = sizex  #- Floor width
        self.sizey = sizey  #- Floor height
        self.Surface2 = pygame.Surface([self.sizex, self.sizey], pygame.SRCALPHA, 32)  #- Create surface for the Floor
        self.Surface2.fill([0, 200, 200])  #- Fill the Floor with a color
        pygame.draw.rect(self.Surface2, [255, 0, 0], [self.Floorspawnlocationx, self.Floorspawnlocationy, self.sizex, self.sizey], 100)  #- Draw a red rectangle (the Floor)
        self.FloorRect2 = self.Surface2.get_rect(x=Floorspawnlocationx, y=Floorspawnlocationy)  #- Set the position of the Floor

    def draw(self, Window):
        """ Drawing the Floor into the window """
        Window.blit(self.Surface2, self.FloorRect2)  #- Blit (draw) the Floor on the screen  

class Player:
    def __init__(self, centerY, centerX, size, Health):
        self.Health = Health   
        self.centerX = centerX   
        self.centerY = centerY
        self.Velocityy = 2
        self.Velocityx = 0   
        self.size = size   
        self.Surface = pygame.Surface([self.size, self.size], pygame.SRCALPHA, 32)    #- Game surface
        self.Surface.fill([200, 200, 200])                    #- Fill surface with a color
        pygame.draw.circle(self.Surface, [255, 0, 0], [self.centerX, self.centerY], self.size)        #- Draw a circle 
        self.PlayerRect = self.Surface.get_rect(x=Playerspawnlocationx, y=Playerspawnlocationy)        #- Set the position of the top-left corner

Player1 = Player(Playerspawnlocationx, Playerspawnlocationy, 10, 1000) #- Note: 'Player1' is now created from the 'Player' class
Floor1 = Floor(400, 300, 500, 300)  #- Initialize Floor1  
#- Initial variable setup
Fps = 120                    #- Game frame rate (frames per second)
SizeFloor = 1

a = [0] * 1000
MainLoop = True                #- Main loop flag

for i in range(1, 1000):  
    RandomFloor = random.randint(-1, 1)
    a[i] = SizeFloor
    SizeFloor = SizeFloor + RandomFloor
    
##== MAIN GAME LOOP
while MainLoop:

    #- Handle user input
    for event in pygame.event.get():            #- Handle input events (keyboard, mouse)
        if event.type == pygame.QUIT:            #- Quit the program if requested (Alt+F4, close button)
            MainLoop = False

    #- Display
    Window.fill([0, 0, 0])                    #- Fill the window with black color

    for i in range(1, 1000):
        Floor1.FloorRect2.x = Floor1.FloorRect2.x + i
        Floor1.draw(Window)  
        #pygame.draw.rect (Window, [255,128,0], [0+i,500+a[i],10,10], 0)

    if Player1.PlayerRect.colliderect(Floor1.FloorRect2):
        Player1.PlayerRect.y = Player1.PlayerRect.y + Player1.Velocityy  #- Prevent player from walking through the floor
  
     
    KeyboardInput = pygame.key.get_pressed()            #- Get the state of the keyboard keys
  
    if KeyboardInput[pygame.K_RIGHT]:                #- If the right arrow key is pressed
        Player1.Velocityx = Player1.Velocityx + 0.03        
    if KeyboardInput[pygame.K_LEFT]:                #- If the left arrow key is pressed
        Player1.Velocityx = Player1.Velocityx - 0.03            
    if KeyboardInput[pygame.K_UP]:                #- If the up arrow key is pressed
        Player1.Velocityy = Player1.Velocityy - 0.03        
    if KeyboardInput[pygame.K_DOWN]:                #- If the down arrow key is pressed
        Player1.Velocityy = Player1.Velocityy + 0.03        
    
    Player1.Velocityy = Player1.Velocityy + 0.006      
    Player1.PlayerRect.x = Player1.PlayerRect.x + Player1.Velocityx  
    Player1.PlayerRect.y = Player1.PlayerRect.y + Player1.Velocityy    
   
    Window.blit(Player1.Surface, Player1.PlayerRect)  #- Draw the player (red circle) on the screen
    
    pygame.display.flip()                    #- Update the display from the memory buffer to the screen

    #- Time delay for the frame rate
    Clock.tick(Fps)                    #- Delay the game loop according to the specified frame rate
