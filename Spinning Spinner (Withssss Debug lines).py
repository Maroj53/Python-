import pygame  # - import graphics module
import math

##== INITIAL PREPARATION
# - Initialize Pygame
pygame.init()  # - initialize the module

class spinner:
    def __init__(self, center_y, center_x, turn_speed, thickness, spinner_png):
        """
        Initializes the spinner object.
        
        Args:
            center_y (float): The y-coordinate of the spinner's center.
            center_x (float): The x-coordinate of the spinner's center.
            turn_speed (float): The speed of rotation in degrees per frame.
            thickness (int): The thickness of the spinner line.
            spinner_png (Surface): The image representing the spinner.
        """
        self.center_x = center_x   
        self.center_y = center_y
        self.turn_speed = turn_speed       
        self.thickness = thickness  
        self.spinner_png = spinner_png
        self.rotated_spinner = None
        self.angle = 0
        self.rotated_image_rect = None

    def change_speed(self, turn_speed):
        """
        Changes the rotation speed of the spinner.
        
        Args:
            turn_speed (float): New speed of rotation in degrees per frame.
        """
        self.turn_speed = turn_speed

    def change_thickness(self, thickness):
        """
        Changes the thickness of the spinner.
        
        Args:
            thickness (int): New thickness of the spinner line.
        """
        self.thickness = thickness

    def change_coordinates(self, coordinates):
        """
        Changes the vertical position of the spinner.
        
        Args:
            coordinates (float): New y-coordinate for the spinner's center.
        """
        self.center_y = coordinates

    def calculate_half_rotation(self):
        """
        Calculates the half rotation (not currently used in the program).
        """
        a = 180 / self.turn_speed

    def rotate_png(self):
        """
        Rotates the spinner image by the current angle.
        Updates the rotated image for display.
        """
        self.rotated_spinner = pygame.transform.rotate(self.spinner_png, self.angle + self.turn_speed)
        self.rotated_image_1 = self.rotated_spinner.convert_alpha()   
        self.rotated_image_rect = self.rotated_image_1.get_rect (centerx=self.center_x, centery=self.center_y) 
        self.angle = self.angle + self.turn_speed

# - Activate graphic window
window_width = 1000  # - fixed width and height of the game window
window_height = 1000
t = 1
i = 0
k = 3
w = 500
window = pygame.display.set_mode([window_width, window_height])  # - activate the screen
pygame.display.set_caption("Pygame Template")  # - window title

spinner_image = pygame.image.load("spinner.png")

spinner_surface = spinner_image.convert_alpha()  # - convert to pygame format
# - Prepare timing
clock = pygame.time.Clock()  # - initialize the timing module
spinner1 = spinner(500, 500, 3, 2, spinner_surface)
# - Initial variable settings
fps = 20  # - number of game ticks per second
main_loop = True  # - execute the main loop

def polar_coordinates(x, y, r, angle):
    """ 
    Calculate coordinates of destination point distant from source point 
    at an angle from x-axis.

    Args:
        x (float): Horizontal rectangular coordinate of initial point.
        y (float): Vertical rectangular coordinate of initial point.
        r (float): Distance from initial point.
        angle (float): Angle of distance line from x-axis clockwise in degrees.

    Returns:
        tuple: Target rectangular coordinates (x2, y2).
    """
    angle_radian = angle / 180 * math.pi  # - convert angle from degrees to radians
    x2 = x + r * math.cos(angle_radian)  # - calculate horizontal target coordinate
    y2 = y + r * math.sin(angle_radian)  # - calculate vertical target coordinate
    return x2, y2

##== MAIN GAME LOOP
while main_loop:
    # - Handle user input
    for event in pygame.event.get():  # - handle input events (keyboard, mouse)
        if event.type == pygame.QUIT:  # -- exit program if requested (Alt+F4, close button)
            main_loop = False

    # - Display
    window.fill([255, 255, 255])  # - fill the window with white

    def spin(i):
        """
        Draws a line from the spinner's center to a calculated point based on the current angle.
        
        Args:
            i (int): The current angle multiplier for rotation.
        """
        x2, y2 = polar_coordinates(10, 10, 30000, i * 20)
        pygame.draw.line(window, [0, 0, 0], [spinner1.center_x, spinner1.center_y], [spinner1.center_x + x2, spinner1.center_y + y2], spinner1.thickness)  # - draw the line from the spinner's center
        window.blit(spinner1.rotated_image_1,spinner1.rotated_image_rect) 
        print(spinner1.rotated_image_rect.centerx)

    keys = pygame.key.get_pressed()  # - get the state of the keyboard
    if keys[pygame.K_UP]:  # - if the up key is pressed
        spin(i)    
        w = w - 3
        spinner1.change_coordinates(w)
    if keys[pygame.K_DOWN]:  # - if the down key is pressed
        w = w + 3
        spinner1.change_coordinates(w)
    if keys[pygame.K_e]:  # - increase thickness
        t = t + 1
        spinner1.change_thickness(t)
    if keys[pygame.K_d]:  # - decrease thickness
        t = t - 1
        spinner1.change_thickness(t)
    if keys[pygame.K_w]:  # - increase speed
        k = k + 1
        spinner1.change_speed(k)
    if keys[pygame.K_s]:  # - decrease speed
        k = k - 1
        spinner1.change_speed(k)
    if keys[pygame.K_RIGHT]:  # - rotate right
        spinner1.rotate_png()
        spin(i)    
        i = i + spinner1.turn_speed    
    if keys[pygame.K_LEFT]:  # - rotate left
        spin(i)    
        i = i - spinner1.turn_speed    

    pygame.display.flip()  # - update the display from memory to screen

    # - Time delay
    clock.tick(fps)  
